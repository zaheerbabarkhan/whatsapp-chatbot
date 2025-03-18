from fastapi import APIRouter, Request

webhook_router = APIRouter()

@webhook_router.post("/webhook")
async def webhook(request: Request):
    try:
        form_data = await request.form()
        parsed_data = dict(form_data)
        print(parsed_data)
    except RuntimeError:
        return {"error": "Invalid or non-form-encoded body"}
    return {"received": form_data}