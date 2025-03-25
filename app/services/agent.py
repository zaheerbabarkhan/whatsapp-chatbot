from vectara_agentic import Agent
from vectara_agentic.tools import ToolsFactory
from .message import validation_and_intention

class BookingAgent:
    def __init__(self):
        self.tools_factory = ToolsFactory()
        
        try:
            self.booking_agent = Agent(
            tools=[self.tools_factory.create_tool(validation_and_intention)],
            custom_instructions="""
                You are a smart assistant that helps classify WhatsApp messages from users interacting with a hotel booking chatbot.

                - To classify a message, you need to determine the user's intention and message validity you can use the tool 'validation_and_intention'.
                - what ever response is provided by the tool just send it in the resopnse.
                """
        )
        except RuntimeError as e:
            print("Failed to initialize the Booking Agent.")
            print(e)
            raise RuntimeError("Failed to initialize the Booking Agent.")

    async  def chat(self, message: str) -> str:
        try:
            response = await self.booking_agent.achat(message)
            return response
        except RuntimeError as e:
            print(e)
            return "Failed to classify the message."