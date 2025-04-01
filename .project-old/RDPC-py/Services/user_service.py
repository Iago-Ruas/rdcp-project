from Class import user_class
from schemas import UserCreator
from Database.postgres import Database
from asyncpg import UniqueViolationError, DataError, PostgresSyntaxError
from fastapi import HTTPException


class UserService:
    def __init__(self, database: Database):
        # Corrigido: armazenar o método execute corretamente
        self._database_execute = database.execute

    async def create_user(self, user: UserCreator):
        _builder = user_class.UserBuilder()
        user_types = {
            "autor".lower(): lambda: _builder.SetName(user.name)
            .SetEmail(user.email)
            .SetPswd(user.pswd)
            .SetUserType(user.type)
            .Build(),
            "revisor".lower(): lambda: _builder.SetName(user.name)
            .SetEmail(user.email)
            .SetPswd(user.pswd)
            .SetUserType(user.type)
            .Build(),
            "editor".lower(): lambda: _builder.SetName(user.name)
            .SetEmail(user.email)
            .SetPswd(user.pswd)
            .SetUserType(user.type)
            .Build(),
        }
        user_to_post = user_types.get(user.type.lower(), lambda: None)()
        if not user_to_post:
            return {
                "error": "Invalid user type",
                "details": "User type is not recognized.",
            }
        result = await self.post_user(user_to_post)
        if "error" in result:
            error_code = self._map_error_to_http_code(result["error"])
            raise HTTPException(status_code=error_code, detail=result["details"])
        return result

    async def post_user(self, user_to_post: UserCreator):
        query = """
                INSERT INTO article (name, pswd, email, type) 
                VALUES ($1, $2, $3, $4) 
                RETURNING id
                """
        try:
            # Executa a query de inserção
            result = await self._database_execute(
                query,
                user_to_post.name,
                user_to_post.pswd,
                user_to_post.email,
                user_to_post.type,
            )
            return {"id": result}
        except UniqueViolationError as e:
            return {"error": "Email already exists.", "details": str(e)}
        except DataError as e:
            return {"error": "Invalid data provided.", "details": str(e)}
        except PostgresSyntaxError as e:
            return {"error": "SQL syntax error.", "details": str(e)}
        except Exception as e:
            return {"error": "An unexpected error occurred.", "details": str(e)}

    def _map_error_to_http_code(self, error: str) -> int:
        """Mapea o tipo de erro para um código HTTP adequado."""
        if "Email already exists" in error:
            return 409
        elif "Invalid data provided" in error:
            return 400
        elif "SQL syntax error" in error:
            return 500
        else:
            return 500
