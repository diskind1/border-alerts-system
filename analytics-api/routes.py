from fastapi import APIRouter
from dal import alerts_by_border_and_priority, top_urgent_zones, distance_distribution, low_visibility_high_activity, hot_zones

router = APIRouter()

@router.get("/analytics/alerts-by-border-and-priority")
def get_alerts_by_border_and_priority():
    return alerts_by_border_and_priority()

@router.get("/analytics/top-urgent-zones")
def get_top_urgent_zones():
    return top_urgent_zones()

@router.get("/analytics/distance-distribution")
def get_distance_distribution():
    return distance_distribution()


@router.get("/analytics/low-visibility-high-activity")
def get_low_visibility_high_activity():
    return low_visibility_high_activity()

@router.get("/analytics/hot-zones")
def get_hot_zones():
    return hot_zones()