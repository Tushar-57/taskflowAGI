from camel.agents import ChatAgent
from camel.messages import BaseMessage
from camel.models import ModelFactory
from camel.types import ModelPlatformType

m1_model = ModelFactory.create(
	model_platform=ModelPlatformType.OLLAMA,
	model_type="llama3.2:3b",
	model_config_dict={"temperature":0.4},
)

assistant_sys_msg = BaseMessage.make_assistant_message(
	role_name="Assistant",
	content="You are a kind helpful assistant.",
)

agent = ChatAgent(assistant_sys_msg, model=m1_model, token_limit=4096)

user_msg = BaseMessage.make_user_message(
	role_name="User", content="What is your name ?"
)


assistant_response = agent.step(user_msg)
print(assistant_response)
