# 🧠 NLP-Powered Code Comment Generator

This app takes code snippets in Python or JavaScript and generates human-readable comments using an NLP model (`Salesforce/codet5-base`). Built with Streamlit, it helps with code understanding, review, and documentation.

## Features

- Paste or upload code
- Choose comment style (inline or block)
- Select code language
- Beautiful custom Streamlit UI
- Export or copy results

## Run It

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Model Used

- [Salesforce/codet5-base](https://huggingface.co/Salesforce/codet5-base)

## License

MIT
