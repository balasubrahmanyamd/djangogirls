
DEFAULT_QUESTIONS = [
    {
        "title": "What's your name?",
        "question_type": "paragraph",
    },
    {
        "title": "Your e-mail address:",
        "question_type": "paragraph",
    },
    {
        "title": "Your phone number:",
        "help_text": "Include your country prefix",
        "question_type": "paragraph",
    },
    {
        "title": "Where are you from?",
        "help_text": "City, Country",
        "question_type": "paragraph",
    },
    {
        "title": "How old are you?",
        "question_type": "paragraph",
        "is_required": False,
    },
    {
        "title": "Which operating system do you use?",
        "question_type": "choices",
        "choices": "Mac OS X; Windows; Linux",
        "has_option_other": True,
    },
    {
        "title": "What is your current level of experience with programming?",
        "question_type": "choices",
        "choices": "I'm a total beginner, I don't know anything about it; I've tried some HTML or CSS before; I've tried some JavaScript before; I've done a few lessons of Python; I've built a website before; I work as a programmer",
        "has_option_other": True,
    },
    {
        "title": "If you checked anything other than beginner, could you tell us a bit more about your programming knowledge?",
        "question_type": "text",
        "is_required": False,
    },
    {
        "title": "What is your current occupation?",
        "help_text": "What is your current job? Are you a student?",
        "question_type": "text",
    },
    {
        "title": "Why do you want the workshop?",
        "help_text": "Tell us about your motivations and aspirations.",
        "question_type": "text",
    },
    {
        "title": "How are you planning to share what you've learnt with others?",
        "help_text": "Django Girls is a volunteer-run organisation and we look for people who are active and can help us help more women get into the field. We want you to share what you learn at the workshop with others in different ways: by organising a Django Girls event in your city, talking about Django Girls on your local meetups, writing a blog or simply teaching your friends.",
        "question_type": "text",
        "is_required": False
    },
    {
        "title": "How did you hear about Django Girls?",
        "help_text": "Django Girls is a volunteer-run organisation and we look for people who are active and can help us help more women get into the field. We want you to share what you learn at the workshop with others in different ways: by organising a Django Girls event in your city, talking about Django Girls on your local meetups, writing a blog or simply teaching your friends.",
        "question_type": "choices",
        "choices": "Facebook; Twitter; From a friend; PyLadies",
        "is_required": False,
        "is_multiple_choice": True,
        "has_option_other": True,
    },
    {
        "title": "I've read and understood the <a href='/pages/coc/'>Django Girls Code of Conduct</a>",
        "question_type": "choices",
        "choices": "Confirm",
        "is_required": True,
        "is_multiple_choice": True,
    }
]
