from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def score_resume(data):
    job_description = open('job_description.txt', 'r').read()
    resume_text = ' '.join(data.values())
    
    content = [job_description, resume_text]
    cv = CountVectorizer().fit_transform(content)
    score = cosine_similarity(cv)[0][1]
    return round(score * 100, 2)