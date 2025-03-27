import os
import json

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def extract_solutions(file_content):
    right_solution = ""
    starting_code = ""
    lines = file_content.split('\n')
    right_solution_started = False
    starting_code_started = False

    for line in lines:
        if "def right_solution" in line:
            right_solution_started = True
            starting_code_started = False
        elif "# import your libraries here" in line:
            starting_code_started = True
            right_solution_started = False

        if right_solution_started:
            right_solution += line + '\n'
        elif starting_code_started:
            starting_code += line + '\n'

    return right_solution.strip(), starting_code.strip()

def convert_problem_to_json(problem_path):
    problem_data = {}
    
    # Read solution.py
    solution_path = os.path.join(problem_path, 'solution.py')
    if os.path.exists(solution_path):
        file_content = read_file(solution_path)
        right_solution, starting_code = extract_solutions(file_content)
        problem_data['right_solution'] = right_solution
        problem_data['starting_code'] = starting_code
    else:
        problem_data['right_solution'] = ""
        problem_data['starting_code'] = ""
    
    # Read problem_statement.md
    problem_statement_path = os.path.join(problem_path, 'problem_statement.md')
    if os.path.exists(problem_statement_path):
        problem_data['description'] = read_file(problem_statement_path)
    else:
        problem_data['description'] = ""
    
    # Read step_by_step_solution.md
    step_by_step_solution_path = os.path.join(problem_path, 'step_by_step_solution.md')
    if os.path.exists(step_by_step_solution_path):
        problem_data['step_by_step_solution'] = read_file(step_by_step_solution_path)
    else:    
        problem_data['step_by_step_solution'] = ""
    
    # Read learn_topic_beforehand.md
    learn_topic_beforehand_path = os.path.join(problem_path, 'learn_topic_beforehand.md')
    if os.path.exists(learn_topic_beforehand_path):
        problem_data['learn_topic_beforehand'] = read_file(learn_topic_beforehand_path)
    else:
        problem_data['learn_topic_beforehand'] = ""

    problem_data_json_path = os.path.join(problem_path, 'problem_data.json')
    if os.path.exists(problem_data_json_path):
        with open(problem_data_json_path, 'r') as file:
            problem_data_json = json.load(file)
            problem_data['test_cases'] = problem_data_json['testcases']
            problem_data['severity'] = problem_data_json['severity']
            problem_data['id'] = problem_data_json['problem_id']
            problem_data['name'] = problem_data_json['name'].title()
    else:
        problem_data['test_cases'] = []
        problem_data['severity'] = ""
        problem_data['id'] = 0
        problem_data['name'] = ""
    
    return problem_data

def convert_problems_to_json(base_path):
    courses = {}
    
    for course_name in sorted(os.listdir(base_path)):
        course_path = os.path.join(base_path, course_name)
        if os.path.isdir(course_path):
            topics = {}
            for topic_name in sorted(os.listdir(course_path)):
                topic_path = os.path.join(course_path, topic_name)
                if os.path.isdir(topic_path):
                    problems = []
                    for problem_name in sorted(os.listdir(topic_path)):
                        problem_path = os.path.join(topic_path, problem_name)
                        if os.path.isdir(problem_path):
                            problem_data = convert_problem_to_json(problem_path)
                            problems.append(problem_data)
                    # Sort problems by id
                    problems.sort(key=lambda x: x['id'])
                    topics[topic_name] = problems
            # Sort topics by key
            sorted_topics = dict(sorted(topics.items(), key=lambda x: int(x[0].split('.')[0])))
            courses[course_name] = sorted_topics
    
    return courses

def save_json(data, file_path):
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    base_path = 'problems'
    output_file = 'problems.json'
    problems_data = convert_problems_to_json(base_path)
    save_json(problems_data, output_file)
    print(f"Problems data saved to {output_file}")