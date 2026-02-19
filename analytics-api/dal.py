from connection import get_conn


def alerts_by_border_and_priority():
    conn = get_conn()
    cur = conn.cursor(dictionary=True)

    cur.execute("""
        
    """,)

    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def top_urgent_zones():
    conn = get_conn()
    cur = conn.cursor(dictionary=True)

    cur.execute("""
        
    """,)

    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def distance_distribution():
    conn = get_conn()
    cur = conn.cursor(dictionary=True)

    cur.execute("""
        
    """,)

    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows


def low_visibility_high_activity():
    conn = get_conn()
    cur = conn.cursor(dictionary=True)

    cur.execute("""
        
    """,)

    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows


def hot_zones():
    conn = get_conn()
    cur = conn.cursor(dictionary=True)

    cur.execute("""
        
    """,)

    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows
