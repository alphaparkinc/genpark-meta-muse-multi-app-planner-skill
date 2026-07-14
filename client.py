class MetaMuseMultiAppPlannerClient:
    def plan_steps(self, apps_list: list[str], task_description: str) -> dict:
        return {"execution_steps": [f"Read from {apps_list[0]}", f"Post results to {apps_list[1]}"]}