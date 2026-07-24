"""
Nilai konstan lintas modul untuk platform OptiCargo.
File ini memastikan tidak ada "magic numbers" yang di-hardcode berulang kali di repo lain.
"""

# API Pagination Defaults (Selaras dengan PageParams di api/pagination.py)
DEFAULT_PAGE_SIZE = 20
MAX_PAGE_SIZE = 100

# Graph Analysis Defaults (Selaras dengan GraphAnalysisInput)
DEFAULT_SEARCH_RADIUS_DAYS = 7