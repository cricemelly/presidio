from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import RecognizerResult, OperatorConfig

# Initialize the engine:
engine = AnonymizerEngine()

# Invoke the anonymize function with the text, 
# analyzer results (potentially coming from presidio-analyzer) and
# Operators to get the anonymization output:
result = engine.anonymize(
    text="My name is cricemelly, cricemelly",
    analyzer_results=[
        RecognizerResult(entity_type="PERSON", start=11, end=16, score=0.8),
        RecognizerResult(entity_type="PERSON", start=17, end=28, score=0.8),
    ],
    operators={"PERSON": OperatorConfig("keep", {"new_value": "BIP"})},
)

print(result)