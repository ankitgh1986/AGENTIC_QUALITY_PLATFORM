# Agentic AI Quality Platform

An Agentic AI Testing and Evaluation Framework that validates LLM responses using multiple specialized agents and provides semantic, risk, judge, and trend-based quality assessments.

## Current Version

v2.3

---

## Architecture

ScenarioGenerationAgent

↓

APIAgent

↓

LLMAgent

↓

SemanticSimilarityAgent

↓

SemanticValidatorAgent

↓

LLMJudgeAgent

↓

EvaluationResult Model

↓

RiskAgent

↓

CSVExportAgent

↓

TrendAnalysisAgent

↓

ReportingAgent

---

## Features

### Scenario Generation

* Automated Scenario Generation
* 300 Test Scenarios
* Happy Path Scenarios
* Variations and Rephrased Queries
* Hinglish Test Cases
* Adversarial Test Cases

### Validation

* API Response Validation
* LLM Response Validation
* Semantic Similarity Scoring
* Rule-Based Validation

### Failure Detection

* Hallucination Detection
* Intent Drift Detection
* Contradiction Detection

### AI Evaluation

* Semantic Score Calculation
* LLM Judge Evaluation
* Judge Score
* Judge Verdict
* Judge Reason

### Risk Assessment

* LOW Risk Classification
* MEDIUM Risk Classification
* HIGH Risk Classification

### Reporting

* CSV Export
* Executive Summary Report
* Pass Rate Calculation
* Failure Breakdown
* GO / NO GO Recommendation

### Historical Analysis

* Historical Run Tracking
* Pass Rate Trend Analysis
* Quality Improvement Tracking

---

## Dataset

### Domain

Telecom

### Supported Intents

* Balance Inquiry
* Data Usage
* Customer Care
* Network Issue
* Bill Payment
* Roaming
* SIM Activation
* Plan Information
* Recharge
* SMS and Calls

### Test Volume

* 10 Intents
* 300 Generated Scenarios

---

## Example Metrics

* Total Scenarios
* Passed Scenarios
* Failed Scenarios
* Pass Rate
* Average Semantic Score
* Average Judge Score
* Failure Type Distribution
* Risk Distribution
* Historical Trends

---

## Sample Output

Pass Rate: 70.00%

Average Semantic Score: 0.68

Average Judge Score: 6.90/10

Hallucinations: 30

Intent Drift: 30

Contradictions: 30

Recommendation: NO GO

---

## Project Structure

AGENTIC_QUALITY_PLATFORM/

├── agents/

├── models/

├── reports/

├── test_data/

├── run.py

├── requirements.txt

└── README.md

---

## Roadmap

### Completed

* v1.0 Core Agent Framework
* v2.0 Semantic Similarity Agent
* v2.1 LLM Judge Agent
* v2.2 EvaluationResult Model
* v2.3 Trend Analysis Agent

### Planned

* v2.4 Confidence Agent
* v2.5 Probabilistic Verification
* v2.6 Multi-Judge Evaluation
* v2.7 Dashboard Metrics Export
* v3.0 Real LLM Integration
