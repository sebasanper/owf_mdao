# -*- coding: utf-8 -*-
"""
Created on Mon Nov 09 14:58:16 2015

@author: Αλβέρτος
"""

from farm_description import Cost1 as cost1


class CostAnalysts:   
    
    def __init__(self, support_team):
        self.support_team = support_team
        self.number_of_turbines = 1
        self.tower_price = cost1(2.04, 'USD', 2002)  # [$/kg]
        self.transition_piece_price = cost1(3.75, 'Euro', 2007)  # [euro/kg]
        self.grout_price = cost1(0.1, 'Euro', 2003)  # [euro/kg] (This value is not supported by literature/data and based on some information on the web about concrete
        self.monopile_price = cost1(2.25, 'Euro', 2007)  # [euro/kg]
        self.scour_protection_per_volume = cost1(211.0, 'Euro', 2003)  # [euro/m^3]
        self.foundation_installation_per_mass = cost1(1.4, 'USD', 2010)  # [$/kg]
        self.scour_protection_removal_per_volume = cost1(33.0, 'USD', 2010)  # [$/m^3]

    def initialyse(self):
        self.set_support_structure_costs()
       
    def set_support_structure_costs(self):
        self.support_team.value.economic.capex.procurement.support_structures.tower = (self.number_of_turbines * self.tower_price.value * self.support_team.properties.support_structure.tower_mass)

        # print self.support_team.value.economic.capex.procurement.support_structures.tower
        self.support_team.value.economic.capex.procurement.support_structures.transition_piece = (self.number_of_turbines * self.transition_piece_price.value * self.support_team.properties.support_structure.transition_piece_mass)

        self.support_team.value.economic.capex.procurement.support_structures.grout = (self.number_of_turbines * self.grout_price.value * self.support_team.properties.support_structure.grout_mass)

        self.support_team.value.economic.capex.procurement.support_structures.monopile = (self.number_of_turbines * self.monopile_price.value * self.support_team.properties.support_structure.pile_mass)

        self.support_team.value.economic.capex.procurement.support_structures.scour_protection = (self.number_of_turbines * self.scour_protection_per_volume.value * self.support_team.properties.support_structure.scour_protection_volume)

        self.support_team.value.economic.capex.installation.foundations = (self.number_of_turbines * self.foundation_installation_per_mass.value * self.support_team.properties.support_structure.pile_mass)

        self.support_team.value.economic.decommissioning.removal.foundations = self.support_team.value.economic.capex.installation.foundations

        self.support_team.value.economic.decommissioning.removal.scour_protection = (self.number_of_turbines * self.scour_protection_removal_per_volume.value * self.support_team.properties.support_structure.scour_protection_volume)

        # print self.support_team.value.economic.capex.procurement.support_structures.tower
        self.support_team.total_support_structure_cost = (self.support_team.value.economic.capex.procurement.support_structures.tower + self.support_team.value.economic.capex.procurement.support_structures.transition_piece + self.support_team.value.economic.capex.procurement.support_structures.grout + self.support_team.value.economic.capex.procurement.support_structures.monopile + self.support_team.value.economic.capex.procurement.support_structures.scour_protection + self.support_team.value.economic.capex.installation.foundations + self.support_team.value.economic.decommissioning.removal.foundations + self.support_team.value.economic.decommissioning.removal.scour_protection)
