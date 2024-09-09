"""
Building a regular expression to make extract hashtags from text:
1. Hashtags will be case insensitive (#ai and #AI will be same)
2. Hashtags having more length than 4 characters will be excluded.
"""
import re

SAMPLE_TEXT = """
#HelloWorld #helloWorld #HELLOWORLD #Hello #HELLO #hello #World #WORLD #world #Programming #PROGRAMMING #programming #Code #CODE #code #Python #PYTHON #python #Java #JAVA #java #JavaScript #JAVASCRIPT #javascript #CodingIsFun #CODINGISFUN #codingisfun #DevLife #DEVLIFE #devlife #Tech #TECH #tech #Developer #DEVELOPER #developer #Software #SOFTWARE #software #Engineer #ENGINEER #engineer #ComputerScience #COMPUTERSCIENCE #computerscience #DataScience #DATASCIENCE #datascience #MachineLearning #MACHINELEARNING #machinelearning #AI #ai #AI #DeepLearning #DEEPLEARNING #deeplearning #NeuralNetworks #NEURALNETWORKS #neuralnetworks #BigData #BIGDATA #bigdata #CloudComputing #CLOUDCOMPUTING #cloudcomputing #Blockchain #BLOCKCHAIN #blockchain #IoT #IOT #iot #CyberSecurity #CYBERSECURITY #cybersecurity #WebDevelopment #WEBDEVELOPMENT #webdevelopment #Frontend #FRONTEND #frontend #Backend #BACKEND #backend #FullStack #FULLSTACK #fullstack #API #api #API #RESTful #RESTFUL #restful #GraphQL #GRAPHQL #graphql #MobileApp #MOBILEAPP #mobileapp #Android #ANDROID #android #iOS #IOS #ios #Swift #SWIFT #swift #Kotlin #KOTLIN #kotlin #ObjectiveC #OBJECTIVEC #objectivec #ReactNative #REACTNATIVE #reactnative #Flutter #FLUTTER #flutter #Unity #UNITY #unity #GameDev #GAMEDEV #gamedev #AugmentedReality #AUGMENTEDREALITY #augmentedreality #VirtualReality #VIRTUALREALITY #virtualreality #DevOps #DEVOPS #devops #CI_CD #ci_cd #CICD #Automation #AUTOMATION #automation #SRE #sre #SRE #InfrastructureAsCode #INFRASTRUCTUREASCODE #infrastructureascode #Microservices #MICROSERVICES #microservices #Containerization #CONTAINERIZATION #containerization #Kubernetes #KUBERNETES #kubernetes #Docker #DOCKER #docker #Serverless #SERVERLESS #serverless #EdgeComputing #EDGECOMPUTING #edgecomputing #QuantumComputing #QUANTUMCOMPUTING #quantumcomputing #5G #5g #5G #Innovation #INNOVATION #innovation #Startups #STARTUPS #startups #Entrepreneurship #ENTREPRENEURSHIP #entrepreneurship #VentureCapital #VENTURECAPITAL #venturecapital #AngelInvesting #ANGELINVESTING #angelinvesting #FinTech #FINTECH #fintech #HealthTech #HEALTHTECH #healthtech #EdTech #EDTECH #edtech #CleanTech #CLEANTECH #cleantech #SpaceTech #SPACETECH #spacetech #GovTech #GOVTECH #govtech #SmartCities #SMARTCITIES #smartcities #AgriTech #AGRITECH #agritech #Robotics #ROBOTICS #robotics #3DPrinting #3DPRINTING #3dprinting #WearableTech #WEARABLETECH #wearabletech #InnovationHub #INNOVATIONHUB #innovationhub #DigitalTransformation #DIGITALTRANSFORMATION #digitaltransformation #FutureOfWork #FUTUREOFWORK #futureofwork
"""

if __name__ == "__main__":
    string_list = SAMPLE_TEXT.split("\n")
    expression = r"#[\w]{4,}"
    out = {}
    for sample in string_list:
        candidate_hashtags = re.findall(pattern= expression, string= sample)
        for cand in candidate_hashtags: 
            if cand.lower() in out: continue
            else: out[cand.lower()] = cand
    
    out_li = list(out.values())
    # print(out_li)
    for i in range((len(out_li) // 5) + 1):
        print(out_li[i * 5: min(i * 5 + 5, len(out_li))])
