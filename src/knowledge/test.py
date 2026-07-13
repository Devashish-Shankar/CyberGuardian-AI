from src.knowledge.attack_database import AttackDatabase
from src.knowledge.knowledge_loader import KnowledgeLoader
from src.knowledge.attack_mapper import AttackMapper
from src.knowledge.severity import SeverityEngine
from src.knowledge.mitigation import MitigationEngine
from src.knowledge.mitre_loader import MitreLoader


def test_attack_database():

    print("=" * 60)

    print("Testing Attack Database")

    print("=" * 60)

    db = AttackDatabase()

    print("Database Size :", db.size())

    print()

    for attack in db.all_attacks():

        print("-", attack)

    print()

    print("Attack Database Passed")



def test_loader():

    print()

    print("=" * 60)

    print("Testing Knowledge Loader")

    print("=" * 60)

    loader = KnowledgeLoader()

    knowledge = loader.load()

    print()

    print(type(knowledge))

    print()

    print(

        "Total Entries:",

        len(knowledge)

    )

    print()

    print("Knowledge Loader Passed")


def test_attack_mapper():

    print()

    print("=" * 60)

    print("Testing Attack Mapper")

    print("=" * 60)

    mapper = AttackMapper()

    attack = mapper.map("DDoS")

    print()

    print("Category :",
          attack["category"])

    print("Severity :",
          attack["severity"])

    print()

    print("Attack Mapper Passed")
    

def test_severity():

    print()

    print("=" * 60)
    print("Testing Severity Engine")
    print("=" * 60)

    mapper = AttackMapper()

    attack = mapper.map("DDoS")

    engine = SeverityEngine()

    severity = engine.get(attack)

    print()

    print("Severity :", severity)

    print()

    print("Severity Engine Passed")
    

def test_mitigation():

    print()

    print("=" * 60)
    print("Testing Mitigation Engine")
    print("=" * 60)

    mapper = AttackMapper()

    attack = mapper.map("DDoS")

    engine = MitigationEngine()

    mitigation = engine.get(attack)

    print()

    print("Mitigation Steps:")

    for step in mitigation:

        print(f"• {step}")

    print()

    print("Mitigation Engine Passed")
    
def test_mitre_loader():

    print()

    print("=" * 60)
    print("Testing MITRE Loader")
    print("=" * 60)

    mapper = AttackMapper()

    attack = mapper.map("PortScan")

    loader = MitreLoader()

    techniques = loader.get(attack)

    print()

    print("MITRE ATT&CK Techniques:")

    for technique in techniques:

        print(f"• {technique}")

    print()

    print("MITRE Loader Passed")

def main():

    test_attack_database()

    test_loader()

    test_attack_mapper()
    
    test_severity()
    
    test_mitigation()
    
    test_mitre_loader()
    
if __name__ == "__main__":

    main()