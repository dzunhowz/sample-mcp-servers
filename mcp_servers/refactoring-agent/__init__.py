"""Refactoring Agent MCP Server"""

try:
    from .main import (
        mcp,
        start_refactoring_job,
        get_job_status,
        get_jobs,
    )
except ImportError:
    # Fallback for environments loading modules from a plain sys.path entry
    from main import (
        mcp,
        start_refactoring_job,
        get_job_status,
        get_jobs,
    )

__all__ = [
    "mcp",
    "start_refactoring_job",
    "get_job_status",
    "get_jobs",
]
