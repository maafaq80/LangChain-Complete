from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline
import os 
import transformers

os.environ['HF_HOME']='D:/huggingface_cache'
llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs=dict(
        temperature=0.7,
        max_new_tokens=50
    )
)

model = ChatHuggingFace(llm=llm)
result = model.invoke("Hello, how are you?")
print(result.content)
print("Result object:", result)
print("Result content:", result.content)