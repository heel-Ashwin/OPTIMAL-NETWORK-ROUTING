def feasibility_analysis():
    budget = float(input("Enter the project budget: "))
    resources_available = input("Are required resources available? (yes/no): ").lower() == "yes"
    technical_expertise = input("Is technical expertise adequate? (yes/no): ").lower() == "yes"
    time_constraints = input("Are there time constraints? (yes/no): ").lower() == "yes"
    
    # Check if budget is sufficient
    if budget < 0:
        return "Budget is negative, project not feasible."
    
    # Check if required resources are available
    if not resources_available:
        return "Required resources are not available, project not feasible."
    
    # Check if technical expertise is adequate
    if not technical_expertise:
        return "Technical expertise is lacking, project not feasible."
    
    # Check if time constraints can be met
    if time_constraints:
        return "Time constraints cannot be met, project not feasible."
    
    # All conditions met, project feasible
    return "Feasibility analysis passed, project feasible."
