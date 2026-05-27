from pydantic import BaseModel,Field
from typing import Dict

class PredictionResponse(BaseModel):
    predicted_category: str = Field(
        ...,
        description="The predicted insurance premium category",
        examples=["High"]
    )
    confidence: float = Field(
        ...,
        description="Model's confidence score for predicted class",
        examples=[0.8432]
    )
    class_probabilities: Dict[str,str] = Field(
        ...,
        description="Probability distribution across all classes",
        examples=["Low:0.01","Medium:0.15","High:0.84"]
    )