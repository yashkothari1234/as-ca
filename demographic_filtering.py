import pandas as pd
import numpy as np

df1 = pd.read_csv('articles.csv')

df1 = df1[df1['eventType'] == 'CONTENT SHARED']

def find_total_events(df1_row):
  total_likes = df1[(df1["contentId"] == df1_row["contentId"]) & (df1["eventType"] == "LIKE")].shape[0]
  total_views = df1[(df1["contentId"] == df1_row["contentId"]) & (df1["eventType"] == "VIEW")].shape[0]
  total_bookmarks = df1[(df1["contentId"] == df1_row["contentId"]) & (df1["eventType"] == "BOOKMARK")].shape[0]
  total_follows = df1[(df1["contentId"] == df1_row["contentId"]) & (df1["eventType"] == "FOLLOW")].shape[0]
  total_comments = df1[(df1["contentId"] == df1_row["contentId"]) & (df1["eventType"] == "COMMENT CREATED")].shape[0]
  return total_likes + total_views + total_bookmarks + total_follows + total_comments

df1["total_events"] = df1.apply(find_total_events, axis=1)

df1 = df1.sort_values(['total_events'], ascending=[False])

output = df1[['eventType','title','text','lang']].head(20).values.tolist()