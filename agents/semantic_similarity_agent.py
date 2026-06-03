from sentence_transformers import SentenceTransformer

from sentence_transformers.util import cos_sim


class SemanticSimilarityAgent:

    def __init__(

        self

    ):

        self.model = SentenceTransformer(

            "all-MiniLM-L6-v2"

        )

    def calculate(

        self,

        expected_text,

        actual_text

    ):

        expected_embedding = (

            self.model.encode(

                expected_text,

                convert_to_tensor=True

            )

        )

        actual_embedding = (

            self.model.encode(

                actual_text,

                convert_to_tensor=True

            )

        )

        similarity = (

            cos_sim(

                expected_embedding,

                actual_embedding

            ).item()

        )

        print(

            "\nSEMANTIC SIMILARITY AGENT"

        )

        print(

            f"\nSimilarity Score: {similarity:.2f}"

        )

        return similarity