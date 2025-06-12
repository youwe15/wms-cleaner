import streamlit as st
import pandas as pd

def map_skus(data, mapping):
    def resolve_msku(sku):
        parts = str(sku).split("+")
        mapped = []
        for p in parts:
            row = mapping[mapping["SKU"].str.lower() == p.strip().lower()]
            if not row.empty:
                mapped.append(row.iloc[0]["MSKU"])
            else:
                mapped.append("UNKNOWN")
        return "+".join(mapped)

    data["Mapped MSKU"] = data["SKU"].apply(resolve_msku)
    return data

st.title("WMS Assignment – SKU to MSKU Mapper")

uploaded_file = st.file_uploader("Upload Sales Data CSV", type="csv")
mapping_file = st.file_uploader("Upload SKU → MSKU Mapping CSV", type="csv")

if uploaded_file and mapping_file:
    sales_df = pd.read_csv(uploaded_file)
    mapping_df = pd.read_csv(mapping_file)
    result = map_skus(sales_df, mapping_df)
    st.dataframe(result)
    csv = result.to_csv(index=False).encode('utf-8')
    st.download_button("Download Cleaned CSV", csv, "cleaned_output.csv", "text/csv")