from mongo_connection import mongo_conn


def alerts_by_border_and_priority():
    col = mongo_conn()
    docs = list(col.find(
        
        ))
    return docs

def top_urgent_zones():
    col = mongo_conn()
    docs = list(col.find(
        
        ))
    return docs


def distance_distribution():
    col = mongo_conn()
    docs = list(col.find(
        
        ))
    return docs


def low_visibility_high_activity():
    col = mongo_conn()
    docs = list(col.find(
        
        ))
    return docs


def hot_zones():
    col = mongo_conn()
    docs = list(col.find(
        
        ))
    return docs

