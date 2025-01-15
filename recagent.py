from base_model import BaseModel
from user_behavior_generator import BehaviorGenerator

class RecAgent(BaseModel):
    def __init__(self, config):
        super().__init__(config)
        self.behavior_generator = BehaviorGenerator(model_name="gpt-3.5-turbo")

    def recommend(self, user_profile, item_pool):
        # 调用生成式模型生成推荐
        return self.behavior_generator.generate_behavior(user_profile, item_pool)
