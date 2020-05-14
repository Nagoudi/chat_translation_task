import os

def get_sample(path, out_path, num=100):
    uttrs = []
    with open(path) as f:
        for i, l in enumerate(f):
            if i <=num:
                uttrs.append(l)
            else:
                break
    with open(out_path, 'w') as f_out:
        for u in uttrs:
            f_out.write(u)
    

get_sample("../chat_translation_task/data/task_data/customer/train_source.txt", "speaker1/main_task_customer_de.txt")
get_sample("../chat_translation_task/data/task_data/customer/train_target.txt", "speaker1/main_task_customer_en.txt")
get_sample("../chat_translation_task/data/task_data/agent/train_source.txt", "speaker2/main_task_agent_en.txt")
get_sample("../chat_translation_task/data/task_data/agent/train_target.txt", "speaker2/main_task_agent_de.txt")

get_sample("../chat_translation_task/data/movie_dialog/user/user.txt", "speaker1/movie_dialog_user_en.txt")
get_sample("../chat_translation_task/data/movie_dialog/assistant/assistant.txt", "speaker2/movie_dialog_assistant_en.txt")

get_sample("../amazon_qa/question/qa_Appliances_question.txt", "speaker1/amazon_question_en.txt")
get_sample("../amazon_qa/answer/qa_Appliances_answer.txt", "speaker2/amazon_answer_en.txt")

get_sample("../amazon_qa/question/qa_Appliances_question.txt", "speaker1/amazon_question_en.txt")
get_sample("../amazon_qa/answer/qa_Appliances_answer.txt", "speaker2/amazon_answer_en.txt")
                
get_sample("../DBDC3/data/user_en.txt", "speaker1/dbdc3_user_en")
get_sample("../DBDC3/data/system_en.txt", "speaker2/dbdc3_system_en")

get_sample("../DBDC4/data/user_en.txt", "speaker1/dbdc4_user_en")
get_sample("../DBDC4/data/system_en.txt", "speaker2/dbdc4_system_en")
