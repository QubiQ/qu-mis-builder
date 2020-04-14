# Copyright 2020 Ferran Sánchez <ferran.sanchez@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "MIS Report Mail",
    "summary": "Allows to send MIS reports by email",
    "version": "11.0.1.0.0",
    "category": "Account",
    "website": "https://www.qubiq.es",
    "author": "QubiQ, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": True,
    "installable": True,
    "depends": [
        "mis_builder"
    ],
    "data": [
        "data/email_template.xml",
        "views/mis_report_instance.xml",
    ],
}
