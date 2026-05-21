branches = [
    {"city": "Minsk", "revenue": 15000},
    {"city": "Warsaw", "revenue": 32000},
    {"city": "London", "revenue": 12000}
]

def audit_logger(func):
    def wrapper(*args, **kwargs):
        print("[AUDIT] Запуск анализа...")
        result = func(*args, **kwargs)
        print("[AUDIT] Анализ завершен.")
        return result
    return wrapper

@audit_logger
def get_sorted_report(branches):
    sorted_branches= sorted(branches, key= lambda item: item["revenue"], reverse=True)
    return sorted_branches

new_branches=get_sorted_report(branches)
print("Топ филиалов:")
print("Топ филиалов:")
for index, branch in enumerate(new_branches, start=1):
    print(f"{index}. {branch['city']}: {branch['revenue']}")