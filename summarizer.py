import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Download required NLTK data
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')


def summarize_text(text):
    if not text or text.strip() == "":
        return "⚠ No input text provided."

    # Tokenize sentences
    sentences = sent_tokenize(text)

    if len(sentences) < 2:
        return text  # Too short to summarize

    # Tokenize words
    words = word_tokenize(text)
    stop_words = set(stopwords.words("english"))

    # Remove stopwords
    filtered_words = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]

    # Build frequency table
    freq_table = {}
    for word in filtered_words:
        freq_table[word] = freq_table.get(word, 0) + 1

    # Score sentences
    sentence_scores = {}
    for sent in sentences:
        for word, freq in freq_table.items():
            if word in sent.lower():
                sentence_scores[sent] = sentence_scores.get(sent, 0) + freq

    # Calculate average score
    if not sentence_scores:
        return "⚠ Could not generate summary."

    average_score = sum(sentence_scores.values()) / len(sentence_scores)

    # Select important sentences
    summary_sentences = [
        sent for sent in sentences
        if sentence_scores.get(sent, 0) >= (1.2 * average_score)
    ]

    # Fallback: if nothing selected, return first 2 sentences
    if not summary_sentences:
        summary_sentences = sentences[:2]

    summary = " ".join(summary_sentences)
    return summary.strip()
