"""
Armageddon Treats — Document Generator
Generates all business plan documents and financial workbook.
Run: python main.py
"""
import os
from armageddon_treats.generators.audit import build_main_document
from armageddon_treats.generators.works_cited import build_works_cited
from armageddon_treats.generators.workbook import build_workbook
from armageddon_treats.generators.modules.module_1 import build_module_1
from armageddon_treats.generators.modules.module_2 import build_module_2
from armageddon_treats.generators.modules.module_3 import build_module_3
from armageddon_treats.generators.modules.module_4 import build_module_4
from armageddon_treats.generators.modules.module_5 import build_module_5

if __name__ == "__main__":
    os.makedirs("output", exist_ok=True)
    print("Generating Armageddon Treats documents...\n")
    print("Business Plan Audit...")
    build_main_document()
    build_works_cited()
    print("Financial Workbook...")
    build_workbook()
    print("Operational Modules...")
    build_module_1()
    build_module_2()
    build_module_3()
    build_module_4()
    build_module_5()
    print("\nAll documents generated in output/")
