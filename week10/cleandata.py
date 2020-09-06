import pandas as pd
from snownlp import SnowNLP
from sqlalchemy import create_engine

# NLP舆情分析函数
def _sentiment(text):
    s = SnowNLP(text)
    return s.sentiments

# mysql数据库配置信息
db_info = {'user': 'root',
           'password': 'root123',
           'host': 'localhost',
           'port': 3306,
           'database': 'test1'
           }

if __name__ == "__main__":
    # 建立mysql数据库连接
    engine = create_engine('mysql+pymysql://%(user)s:%(password)s@%(host)s:%(port)d/%(database)s?charset=utf8' % db_info, encoding='utf-8')

    # 一、处理评论信息
    # 加载评论信息
    sql_comment= 'SELECT * FROM pinglun'
    df_com = pd.read_sql(sql_comment,engine)

    # 处理重复的评论信息
    df_com.drop_duplicates(subset=None, keep='first', inplace=True)

    # 清理评论内容为空值的信息
    df_com.drop(labels = (df_com[df_com['comment'] == ""].index), axis = 0,inplace= True)

    # 为评论信息添加舆情分析判断
    df_com["sentiment"] = df_com.comment.apply(_sentiment)

    # 将清洗后的评论数据存入mysql
    df_com.to_sql('zdm_comment_clean', engine, if_exists='replace', index=False)

    # 二、加载品牌信息
    sql_product = 'SELECT * from phone_info'

    df_pro = pd.read_sql(sql_product,engine)

    # 三、将品牌信息与评论信息融合，形成完整的品牌舆情信息
    df_pro_com = df_com.merge(df_pro,  on='uid')
    
    # 将处理完毕的品牌舆情信息存入mysql数据库持久化保存
    m=df_pro_com.to_sql('zdm_pro_com', engine, if_exists='replace', index=True)
    #m = df_pro_com[['id','datePublished','comment','sentiment','bandname','platform','publisher']].to_sql('zdm_pro_com', engine, if_exists='replace', index=True)
    print(f'数据处理完毕：{m}') 