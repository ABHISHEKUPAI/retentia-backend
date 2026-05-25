from sqlalchemy.orm import Session
from app import models


def get_syllabus(db: Session):
    subjects = db.query(models.Subject).all()

    result = []

    for subject in subjects:
        subject_data = {
            "name": subject.name,
            "topics": []
        }

        topics = db.query(models.Topic).filter_by(subject_id=subject.id).all()

        for topic in topics:
            topic_data = {
                "name": topic.name,
                "chapters": []
            }

            chapters = db.query(models.Chapter).filter_by(topic_id=topic.id).all()

            for chapter in chapters:
                chapter_data = {
                    "name": chapter.name,
                    "concepts": []
                }

                concepts = db.query(models.Concept).filter_by(chapter_id=chapter.id).all()

                for concept in concepts:
                    chapter_data["concepts"].append({
                        "name": concept.name
                    })

                topic_data["chapters"].append(chapter_data)

            subject_data["topics"].append(topic_data)

        result.append(subject_data)

    return result
