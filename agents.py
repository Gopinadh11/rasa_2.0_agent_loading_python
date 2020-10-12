from rasa.core.agent import Agent
import os
import asyncio
from rasa.core.utils import EndpointConfig
from rasa.core.interpreter import RasaNLUInterpreter
#interpreter = RasaNLUInterpreter(
#"examples/restaurantbot/models/nlu/current")
#action_endpoint = 'http://127.0.0.1:5005'
# async def load_agent():
#     agent = Agent
#     await asyncio.sleep(5)
#     agent.load("C:/Users/Gopi/Desktop/rasa/rasa_2_version/models/20201010-155216.tar.gz")
#     agent.handle_text(self= None,text_message="hello",output_channel=None,sender_id=None)
#
#
# asyncio.run(load_agent())
# async def load_agent():
#     model_path = "C:/Users/Gopi/Desktop/rasa/rasa_2_version/models/20201010-155216.tar.gz"
#     agent = await Agent.load_data(training_resource=model_path,remove_duplicates=None)
#     agent.handle_text(text_message='hello')
#
# asyncio.run(load_agent())
async def load_agent():
    model_path = "C:/Users/Gopi/Desktop/rasa/rasa_2_version/models/20201010-155216.tar.gz"
    agent =  Agent.load(model_path)
    agent_reply = await agent.handle_text('hello')
    print(agent)
    print(agent_reply)

asyncio.run(load_agent())

#async load_data(training_resource: Union[Text, TrainingDataImporter], remove_duplicates: bool = True, unique_last_num_states: Optional[int] = None, augmentation_factor: int = 50, tracker_limit: Optional[int] = None, use_story_concatenation: bool = True, debug_plots: bool = False, exclusion_percentage: Optional[int] = None) -> List[DialogueStateTracker]
# from rasa.core.agent import Agent
# from rasa.core.policies import FallbackPolicy, KerasPolicy, MemoizationPolicy, FormPolicy
# from rasa.core.interpreter import RasaNLUInterpreter
# from rasa.core.training import interactive
# from rasa.core.utils import EndpointConfig
#
# logger = logging.getLogger(__name__)
#
# # this will catch predictions the model isn't very certain about
# # there is a threshold for the NLU predictions as well as the action predictions
# fallback = FallbackPolicy(fallback_action_name="utter_unclear",
#                           core_threshold=0.2,
#                           nlu_threshold=0.1)
#
# def train_dialogue(interpreter,domain_file = 'domain.yml',
#                    model_path = './models/dialogue',
#                    training_data_file = './data/stories.md'):
#
#     #action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
#     agent = Agent(domain_file, policies=[MemoizationPolicy(), KerasPolicy(), FormPolicy(), fallback])
#     training_data = agent.load_data('./data/stories.md')
#
#     agent.train(training_data)
#
#     agent.persist('models/dialogue')
#     return agent
#
# def run_weather_bot(serve_forever=True):
#     nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/current')
#     action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
#     agent = Agent.load('./models/dialogue', interpreter=nlu_interpreter, action_endpoint=action_endpoint)
#     #rasa_core.run.serve_application(agent ,channel='cmdline')
#
#     return agent
#
# if __name__ == '__main__':
#     train_dialogue(interpreter=RasaNLUInterpreter)
#     run_weather_bot()