from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate


def generate_pet_name(animal_type: str, pet_colour: str) -> str:
    llm = ChatOllama(model="llama3", temperature=0.7)

    prompt = PromptTemplate(
        input_variables=["animal_type", "pet_colour"],
        template=(
            "I have a {animal_type} pet. "
            "It is {pet_colour} in color. "
            "Suggest five cool pet names. "
            "Return only the names as a numbered list."
        )
    )

    chain = prompt | llm
    response = chain.invoke(
        {"animal_type": animal_type, "pet_colour": pet_colour}
    )

    return response.content