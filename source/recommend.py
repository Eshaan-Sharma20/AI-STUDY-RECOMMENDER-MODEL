def generate_study_plan(level):
    if level == "weak":
        return "You should focus more: Study 2-3 hours daily, revise basics, and practice easy questions."
    
    elif level == "medium":
        return "Keep practicing: Study 1-2 hours daily and improve problem-solving skills."
    
    elif level == "strong":
        return "You're doing great: Revise concepts and try advanced-level problems."
    
    else:
        return "Unable to generate recommendation."
