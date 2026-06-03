from agents.scenario_generation_agent import (
    ScenarioGenerationAgent
)

from agents.orchestrator_agent import (
    OrchestratorAgent
)

from agents.reporting_agent import (
    ReportingAgent
)

from agents.csv_export_agent import (
    CSVExportAgent
)


generator = ScenarioGenerationAgent()

orchestrator = OrchestratorAgent()

reporter = ReportingAgent()

csv_exporter = CSVExportAgent()


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

        "\n----------------------"

    )


csv_exporter.export(

    results

)

reporter.generate(

    results

)