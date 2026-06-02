from agents.scenario_generation_agent import (
    ScenarioGenerationAgent
)

from agents.orchestrator_agent import (
    OrchestratorAgent
)

from agents.reporting_agent import (
    ReportingAgent
)


generator = ScenarioGenerationAgent()

orchestrator = OrchestratorAgent()

reporter = ReportingAgent()


scenarios = generator.generate()

results = []


for scenario in scenarios:

    result = orchestrator.execute(

        scenario

    )

    results.append(

        result

    )

    print(

        f"\nFinal Result: {result['result']}"

    )

    print(

        "\n----------------------"

    )


reporter.generate(

    results

)