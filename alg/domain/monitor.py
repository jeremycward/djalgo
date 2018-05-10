from random import randint
from datetime import datetime
from datetime import timedelta


class Idx:
    def __init__(self, name, jobs):
        self.name = name
        self.jobs = jobs


def lcEvt(name, minsDiff):
    return LifeCycleEvent(name, datetime.now() + timedelta(minutes=minsDiff))


class Definition:

    def __init__(self, name):
        self.name = name


class JobDefinition(Definition):
    def __init__(self, name, phases):
        Definition.__init__(self, name)
        self.phases = phases


class JobPhaseDefinition(Definition):
    def __init__(self, name,template):
        Definition.__init__(self, name)
        self.details_template = template


class LifeCycleEvent(Definition):
    def __init__(self, name):
        Definition.__init__(self, name)


class Slice:
    def __init__(self, type, value):
        self.type = type
        self.value = value


class JobPhase:
    def __init__(self, phaseDefn):
        self.phaseDefinition = phaseDefn

    def slices(self):
        return [
            Slice("waiting", randint(0, 100)),
            Slice("error", randint(0, 100)),
            Slice("warn", randint(0, 100)),
            Slice("success", randint(0, 100))
        ]

class Job:
    def __init__(self, definition, id, lifeCycleEvents):
        self.lifeCycleEvents = lifeCycleEvents
        self.definition = definition
        self.id = id
        self.phases = []
        for phaseDefinition in self.definition.phases:
            self.phases.append(JobPhase(phaseDefinition))

    def phases(self):
        return self.phases()


class LifeCycleEvent:
    def __init__(self, type, timeStamp):
        self.type = type
        self.timeStamp = timeStamp


class Monitor:
    def __init__(self):
        self.job_phase_defintions = [
            JobPhaseDefinition("Data Preparation","alg/monitor/detail/data_preparation.html"),
            JobPhaseDefinition("Calculation","alg/monitor/detail/calculation.html"),
            JobPhaseDefinition("Post Processing","alg/monitor/detail/post_processing.html"),
            JobPhaseDefinition("Publication","alg/monitor/detail/publication.html"),
            JobPhaseDefinition("Client Reporting", "alg/monitor/detail/publication.html")
        ]

        self.job_definitions = [
            JobDefinition("0530 Intraday", self.job_phase_defintions[0:4]),
            JobDefinition("0600 DataCheck", self.job_phase_defintions[0:1]),
            JobDefinition("1530 Intraday", self.job_phase_defintions[0:4]),
            JobDefinition("1533 Intraday", self.job_phase_defintions[0:4]),
            JobDefinition("1600 EOD", self.job_phase_defintions[0:5])
        ]

        self.jobs = [
            Job(self.job_definitions[0], randint(0, 10000), [
                lcEvt("scheduled", 50),
                lcEvt("active", 55),
                lcEvt("success", 65)
            ]),
            Job(self.job_definitions[1], randint(0, 10000), [
                lcEvt("scheduled", 60),
                lcEvt("active", 65),
                lcEvt("success", 75)
            ]),
            Job(self.job_definitions[2], randint(0, 10000), [
                lcEvt("scheduled", 70),
                lcEvt("active", 85),
                lcEvt("success", 95)
            ]),

            Job(self.job_definitions[3], randint(0, 10000), [
                lcEvt("scheduled", 70),
                lcEvt("active", 85),
                lcEvt("success", 95)
            ]),

            Job(self.job_definitions[4], randint(0, 10000), [
                lcEvt("scheduled", 70),
                lcEvt("active", 85),
                lcEvt("success", 95)
            ])

        ]

    def report(self):
        return self.jobs
