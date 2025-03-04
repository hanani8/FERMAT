from steps import Step_2_1
from typing import Any


from client import client

class Llama_Step_2_1(Step_2_1):

    def hit(self, image_url: str) -> Any:
        image = self.encode_image(image_url)


        chat_response = client.chat.completions.create(
            model=self.model_path,
            max_tokens=self.max_tokens,
            temperature=self.temperature,
            messages=[
                {
                "role": "user",
                "content": [
                    {"type": "text", "text": self.user_prompt},
                    {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{image}"}},
                ],
            }]
        )
        return(chat_response.choices[0].message.content)