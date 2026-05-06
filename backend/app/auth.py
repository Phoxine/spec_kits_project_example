# Placeholder for JWT authentication
# In POC, roles are mocked via headers

from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()

def get_current_user_role(credentials: HTTPAuthorizationCredentials = Depends(security)):
    # Mock: check token for role
    # In real, decode JWT and get role
    token = credentials.credentials
    if token == "admin":
        return "admin"
    elif token == "cashier":
        return "cashier"
    else:
        raise HTTPException(status_code=401, detail="Invalid token")

def require_admin(role: str = Depends(get_current_user_role)):
    if role != "admin":
        raise HTTPException(status_code=403, detail="Admin required")
    return role

def require_cashier_or_admin(role: str = Depends(get_current_user_role)):
    if role not in ["cashier", "admin"]:
        raise HTTPException(status_code=403, detail="Unauthorized")
    return role