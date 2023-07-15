from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class Issue(BaseModel):
    message: str = Field(..., description="The error message")
    timestamp: datetime = Field(..., description="The time the error occurred")
    stack_trace: str = Field(..., description="The stack trace of the error")
    os: Optional[str] = Field(
        None, description="The operating system where the error occurred"
    )
    browser: Optional[str] = Field(
        None, description="The browser where the error occurred"
    )
    version: Optional[str] = Field(
        None, description="The version of the application where the error occurred"
    )
