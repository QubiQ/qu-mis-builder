# Copyright 2021 Marçal Isern <marsal.isern@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Mis Report Comment",
    "summary": "Add comments on mis report instance",
    "version": "14.0.1.0.0",
    "category": "Accounting",
    "website": "https://www.qubiq.es",
    "author": "QubiQ",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "mis_builder"
    ],
    "data": [
        "views/mis_report_instance.xml",
    ],
}
