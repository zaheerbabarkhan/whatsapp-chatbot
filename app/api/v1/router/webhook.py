from fastapi import APIRouter, Depends, Request

from app.services.agent import BookingAgent

webhook_router = APIRouter()

@webhook_router.post("/webhook")
async def webhook(request: Request, booking_agent: BookingAgent = Depends()):
    try:
        form_data = await request.form()
        parsed_data = dict(form_data)
        print(parsed_data)
        response = await booking_agent.chat(parsed_data["Body"])
        print(response)
    except RuntimeError as e:
        print(e)
        return {"error": "Invalid or non-form-encoded body"}
    return {"received": form_data}