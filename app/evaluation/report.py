import pandas as pd


class ReportGenerator:

    @staticmethod
    def generate(results):

        df=pd.DataFrame(results)

        print(df)

        print("\n")

        print("="*80)

        print("Average Similarity :",round(df["similarity"].mean(),3))

        print("Average Precision :",round(df["precision"].mean(),3))

        print("Average Recall :",round(df["recall"].mean(),3))

        print("Average Confidence :",round(df["confidence"].mean(),3))

        print("Average Latency :",round(df["latency"].mean(),3),"seconds")

        print("="*80)

        df.to_csv(
            "evaluation_results.csv",
            index=False
        )