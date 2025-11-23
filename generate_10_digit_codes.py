#!/usr/bin/env python3
"""
NAICS 10-Digit Code Generator
Manually crafted extensions based on deep industry knowledge
Each sector has custom logic for contextually appropriate granularity
"""

import csv
import os
from typing import List, Dict, Tuple

class NAICS10DigitGenerator:
    """Generate 10-digit NAICS codes with industry-specific granularity"""

    def __init__(self, input_file: str):
        self.input_file = input_file
        self.output_data = []

    def generate_extensions(self, row: Dict) -> List[Dict]:
        """
        Generate 10-digit extensions for an 8-digit code
        Returns list of 10-digit code dictionaries
        """
        naics_6 = row['NAICS_6_Digit']
        naics_8 = row['NAICS_8_Digit']
        title_8 = row['NAICS_8_Title']
        criteria_8 = row['Differentiation_Criteria']
        desc_8 = row['Description']

        # Determine sector from first 2 digits
        sector = naics_6[:2]

        # Route to sector-specific generator
        if sector == '11':
            return self.generate_agriculture(naics_6, naics_8, title_8, criteria_8, desc_8)
        elif sector == '21':
            return self.generate_mining(naics_6, naics_8, title_8, criteria_8, desc_8)
        elif sector == '22':
            return self.generate_utilities(naics_6, naics_8, title_8, criteria_8, desc_8)
        elif sector == '23':
            return self.generate_construction(naics_6, naics_8, title_8, criteria_8, desc_8)
        elif sector in ['31', '32', '33']:
            return self.generate_manufacturing(naics_6, naics_8, title_8, criteria_8, desc_8)
        elif sector == '42':
            return self.generate_wholesale(naics_6, naics_8, title_8, criteria_8, desc_8)
        elif sector in ['44', '45']:
            return self.generate_retail(naics_6, naics_8, title_8, criteria_8, desc_8)
        elif sector in ['48', '49']:
            return self.generate_transportation(naics_6, naics_8, title_8, criteria_8, desc_8)
        elif sector == '51':
            return self.generate_information(naics_6, naics_8, title_8, criteria_8, desc_8)
        elif sector == '52':
            return self.generate_finance(naics_6, naics_8, title_8, criteria_8, desc_8)
        elif sector == '53':
            return self.generate_realestate(naics_6, naics_8, title_8, criteria_8, desc_8)
        elif sector == '54':
            return self.generate_professional(naics_6, naics_8, title_8, criteria_8, desc_8)
        elif sector == '55':
            return self.generate_management(naics_6, naics_8, title_8, criteria_8, desc_8)
        elif sector == '56':
            return self.generate_administrative(naics_6, naics_8, title_8, criteria_8, desc_8)
        elif sector == '61':
            return self.generate_education(naics_6, naics_8, title_8, criteria_8, desc_8)
        elif sector == '62':
            return self.generate_healthcare(naics_6, naics_8, title_8, criteria_8, desc_8)
        elif sector == '71':
            return self.generate_arts(naics_6, naics_8, title_8, criteria_8, desc_8)
        elif sector == '72':
            return self.generate_accommodation(naics_6, naics_8, title_8, criteria_8, desc_8)
        elif sector == '81':
            return self.generate_other_services(naics_6, naics_8, title_8, criteria_8, desc_8)
        elif sector == '92':
            return self.generate_public_admin(naics_6, naics_8, title_8, criteria_8, desc_8)
        else:
            return self.generate_generic(naics_8, title_8, criteria_8, desc_8)

    # ========== SECTOR 11: AGRICULTURE, FORESTRY, FISHING & HUNTING ==========

    def generate_agriculture(self, naics_6: str, naics_8: str, title_8: str,
                            criteria_8: str, desc_8: str) -> List[Dict]:
        """Generate 10-digit codes for agriculture sector with farm-specific granularity"""
        extensions = []

        # Determine sub-industry from NAICS-6
        subsector = naics_6[2:4]

        # Crop Production (111)
        if subsector == '11':
            extensions = self.generate_crop_production(naics_6, naics_8, title_8, criteria_8, desc_8)
        # Animal Production (112)
        elif subsector == '12':
            extensions = self.generate_animal_production(naics_6, naics_8, title_8, criteria_8, desc_8)
        # Forestry (113)
        elif subsector == '13':
            extensions = self.generate_forestry(naics_6, naics_8, title_8, criteria_8, desc_8)
        # Fishing, Hunting, Trapping (114)
        elif subsector == '14':
            extensions = self.generate_fishing_hunting(naics_6, naics_8, title_8, criteria_8, desc_8)
        # Support Activities for Agriculture (115)
        elif subsector == '15':
            extensions = self.generate_ag_support(naics_6, naics_8, title_8, criteria_8, desc_8)
        else:
            extensions = self.generate_generic_ag(naics_8, title_8, criteria_8, desc_8)

        return extensions

    def generate_crop_production(self, naics_6: str, naics_8: str, title_8: str,
                                 criteria_8: str, desc_8: str) -> List[Dict]:
        """Generate crop production specific 10-digit codes"""
        extensions = []

        # For farming operations, key dimensions are:
        # - Farm size/scale (acres, production volume)
        # - Technology adoption (precision ag, conventional, regenerative)
        # - Market channel (commodity, direct-to-consumer, contract, export)
        # - Sustainability practices (water conservation, soil health)

        # Identify key characteristics from the 8-digit title
        title_lower = title_8.lower()

        # Check if it's organic
        is_organic = 'organic' in title_lower
        # Check if it's specialty/premium
        is_specialty = any(word in title_lower for word in ['specialty', 'heirloom', 'identity preserved', 'premium'])
        # Check if it's seed production
        is_seed = 'seed' in title_lower and 'production' in title_lower

        if is_seed:
            # Seed production has different dimensions
            extensions = [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Foundation Seed",
                    'Differentiation_Criteria_10': 'Seed Class',
                    'Description_10': f"{desc_8} Specifically foundation/breeder seed for seed companies."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Certified Seed",
                    'Differentiation_Criteria_10': 'Seed Class',
                    'Description_10': f"{desc_8} Certified seed production for commercial planting."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Hybrid Seed Development",
                    'Differentiation_Criteria_10': 'Seed Type',
                    'Description_10': f"{desc_8} Specializing in hybrid seed research and production."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Contract Seed Growing",
                    'Differentiation_Criteria_10': 'Business Model',
                    'Description_10': f"{desc_8} Contract growing for major seed companies."
                }
            ]
        elif is_organic:
            # Organic farming extensions
            extensions = [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Small-Scale (<50 acres)",
                    'Differentiation_Criteria_10': 'Farm Size',
                    'Description_10': f"{desc_8} Small organic operations under 50 acres, often direct-to-consumer."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Medium-Scale (50-500 acres)",
                    'Differentiation_Criteria_10': 'Farm Size',
                    'Description_10': f"{desc_8} Medium-sized organic farms 50-500 acres with regional distribution."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Large-Scale (500+ acres)",
                    'Differentiation_Criteria_10': 'Farm Size',
                    'Description_10': f"{desc_8} Large organic operations over 500 acres with national distribution."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Regenerative/Biodynamic",
                    'Differentiation_Criteria_10': 'Production Method',
                    'Description_10': f"{desc_8} Advanced organic practices including biodynamic or regenerative agriculture."
                },
                {
                    'NAICS_10_Digit': naics_8 + '05',
                    'NAICS_10_Title': f"{title_8} - Direct-to-Consumer",
                    'Differentiation_Criteria_10': 'Market Channel',
                    'Description_10': f"{desc_8} Organic farms selling primarily through CSA, farmers markets, or farm stands."
                }
            ]
        elif is_specialty:
            # Specialty crop extensions
            extensions = [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Boutique Production",
                    'Differentiation_Criteria_10': 'Scale',
                    'Description_10': f"{desc_8} Small-batch specialty production for premium markets."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Export-Focused",
                    'Differentiation_Criteria_10': 'Market Channel',
                    'Description_10': f"{desc_8} Specialty production focused on international export markets."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Certified/Traceable",
                    'Differentiation_Criteria_10': 'Certification Level',
                    'Description_10': f"{desc_8} Specialty production with premium certifications and full traceability."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Research/Experimental",
                    'Differentiation_Criteria_10': 'Production Purpose',
                    'Description_10': f"{desc_8} Specialty cultivation for research, variety trials, or new market development."
                }
            ]
        else:
            # Standard crop production (conventional, GMO, etc.)
            extensions = [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Small Farm (<100 acres)",
                    'Differentiation_Criteria_10': 'Farm Size',
                    'Description_10': f"{desc_8} Small-scale operations under 100 acres."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Medium Farm (100-1000 acres)",
                    'Differentiation_Criteria_10': 'Farm Size',
                    'Description_10': f"{desc_8} Medium-sized operations 100-1000 acres."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Large Farm (1000+ acres)",
                    'Differentiation_Criteria_10': 'Farm Size',
                    'Description_10': f"{desc_8} Large-scale commercial operations over 1000 acres."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Precision Agriculture",
                    'Differentiation_Criteria_10': 'Technology Level',
                    'Description_10': f"{desc_8} Operations utilizing GPS, sensors, drones, and precision ag technology."
                },
                {
                    'NAICS_10_Digit': naics_8 + '05',
                    'NAICS_10_Title': f"{title_8} - Contract Growing",
                    'Differentiation_Criteria_10': 'Business Model',
                    'Description_10': f"{desc_8} Contract production for processors, cooperatives, or major buyers."
                }
            ]

        return extensions

    def generate_animal_production(self, naics_6: str, naics_8: str, title_8: str,
                                   criteria_8: str, desc_8: str) -> List[Dict]:
        """Generate animal production specific 10-digit codes"""
        extensions = []

        title_lower = title_8.lower()

        # Check type of animal operation
        is_cattle = any(word in title_lower for word in ['cattle', 'beef', 'cow', 'heifer'])
        is_dairy = 'dairy' in title_lower
        is_poultry = any(word in title_lower for word in ['chicken', 'poultry', 'broiler', 'layer', 'turkey'])
        is_swine = any(word in title_lower for word in ['hog', 'pig', 'swine', 'pork'])
        is_specialty = any(word in title_lower for word in ['organic', 'grass-fed', 'free-range', 'pasture'])

        if is_dairy:
            # Dairy-specific extensions
            extensions = [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Small Herd (<100 cows)",
                    'Differentiation_Criteria_10': 'Herd Size',
                    'Description_10': f"{desc_8} Small dairy operations with fewer than 100 milking cows."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Medium Herd (100-500 cows)",
                    'Differentiation_Criteria_10': 'Herd Size',
                    'Description_10': f"{desc_8} Medium dairy operations with 100-500 milking cows."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Large Herd (500+ cows)",
                    'Differentiation_Criteria_10': 'Herd Size',
                    'Description_10': f"{desc_8} Large commercial dairy operations with over 500 milking cows."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Robotic Milking Systems",
                    'Differentiation_Criteria_10': 'Technology Level',
                    'Description_10': f"{desc_8} Dairies utilizing automated robotic milking technology."
                },
                {
                    'NAICS_10_Digit': naics_8 + '05',
                    'NAICS_10_Title': f"{title_8} - Grazing-Based Systems",
                    'Differentiation_Criteria_10': 'Production System',
                    'Description_10': f"{desc_8} Pasture-based dairy systems with seasonal or year-round grazing."
                }
            ]
        elif is_poultry:
            # Poultry-specific extensions
            extensions = [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Small Flock (<10,000 birds)",
                    'Differentiation_Criteria_10': 'Flock Size',
                    'Description_10': f"{desc_8} Small poultry operations with fewer than 10,000 birds."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Medium Operation (10K-100K birds)",
                    'Differentiation_Criteria_10': 'Flock Size',
                    'Description_10': f"{desc_8} Medium-scale operations with 10,000-100,000 birds."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Large CAFO (100K+ birds)",
                    'Differentiation_Criteria_10': 'Flock Size',
                    'Description_10': f"{desc_8} Large concentrated animal feeding operations with over 100,000 birds."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Contract Growing",
                    'Differentiation_Criteria_10': 'Business Model',
                    'Description_10': f"{desc_8} Contract poultry growing for major integrators or processors."
                },
                {
                    'NAICS_10_Digit': naics_8 + '05',
                    'NAICS_10_Title': f"{title_8} - Vertically Integrated",
                    'Differentiation_Criteria_10': 'Integration Level',
                    'Description_10': f"{desc_8} Fully integrated operations including breeding, growing, and processing."
                }
            ]
        elif is_cattle:
            # Beef cattle extensions
            extensions = [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Small Ranch (<100 head)",
                    'Differentiation_Criteria_10': 'Herd Size',
                    'Description_10': f"{desc_8} Small cattle operations with fewer than 100 head."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Medium Ranch (100-500 head)",
                    'Differentiation_Criteria_10': 'Herd Size',
                    'Description_10': f"{desc_8} Medium cattle ranches with 100-500 head."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Large Ranch (500+ head)",
                    'Differentiation_Criteria_10': 'Herd Size',
                    'Description_10': f"{desc_8} Large commercial cattle operations with over 500 head."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Feedlot Finishing",
                    'Differentiation_Criteria_10': 'Production Stage',
                    'Description_10': f"{desc_8} Operations specializing in feedlot finishing of cattle."
                },
                {
                    'NAICS_10_Digit': naics_8 + '05',
                    'NAICS_10_Title': f"{title_8} - Direct-to-Consumer Sales",
                    'Differentiation_Criteria_10': 'Market Channel',
                    'Description_10': f"{desc_8} Operations selling beef directly to consumers, restaurants, or local markets."
                }
            ]
        elif is_swine:
            # Swine-specific extensions
            extensions = [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Small Operation (<100 head)",
                    'Differentiation_Criteria_10': 'Operation Size',
                    'Description_10': f"{desc_8} Small hog operations with fewer than 100 head."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Medium Operation (100-1000 head)",
                    'Differentiation_Criteria_10': 'Operation Size',
                    'Description_10': f"{desc_8} Medium-scale operations with 100-1000 head."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Large CAFO (1000+ head)",
                    'Differentiation_Criteria_10': 'Operation Size',
                    'Description_10': f"{desc_8} Large concentrated operations with over 1000 head."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Farrow-to-Finish",
                    'Differentiation_Criteria_10': 'Production System',
                    'Description_10': f"{desc_8} Complete production from breeding through market weight."
                },
                {
                    'NAICS_10_Digit': naics_8 + '05',
                    'NAICS_10_Title': f"{title_8} - Specialized Production Stage",
                    'Differentiation_Criteria_10': 'Production Stage',
                    'Description_10': f"{desc_8} Specialized in one stage: farrowing, nursery, or finishing."
                }
            ]
        else:
            # Generic animal production
            extensions = self.generate_generic_livestock(naics_8, title_8, criteria_8, desc_8)

        return extensions

    def generate_generic_livestock(self, naics_8: str, title_8: str,
                                   criteria_8: str, desc_8: str) -> List[Dict]:
        """Generic livestock extensions for uncommon animals"""
        return [
            {
                'NAICS_10_Digit': naics_8 + '01',
                'NAICS_10_Title': f"{title_8} - Small-Scale Artisanal",
                'Differentiation_Criteria_10': 'Operation Scale',
                'Description_10': f"{desc_8} Small artisanal operations focused on quality over volume."
            },
            {
                'NAICS_10_Digit': naics_8 + '02',
                'NAICS_10_Title': f"{title_8} - Commercial Production",
                'Differentiation_Criteria_10': 'Operation Scale',
                'Description_10': f"{desc_8} Commercial-scale production for commodity markets."
            },
            {
                'NAICS_10_Digit': naics_8 + '03',
                'NAICS_10_Title': f"{title_8} - Premium/Specialty Market",
                'Differentiation_Criteria_10': 'Market Positioning',
                'Description_10': f"{desc_8} Premium production for specialty or export markets."
            },
            {
                'NAICS_10_Digit': naics_8 + '04',
                'NAICS_10_Title': f"{title_8} - Breeding Stock Production",
                'Differentiation_Criteria_10': 'Production Purpose',
                'Description_10': f"{desc_8} Specialized in producing breeding stock for other operations."
            }
        ]

    def generate_forestry(self, naics_6: str, naics_8: str, title_8: str,
                         criteria_8: str, desc_8: str) -> List[Dict]:
        """Generate forestry-specific 10-digit codes"""
        return [
            {
                'NAICS_10_Digit': naics_8 + '01',
                'NAICS_10_Title': f"{title_8} - Small Woodlot (<100 acres)",
                'Differentiation_Criteria_10': 'Forest Size',
                'Description_10': f"{desc_8} Small private woodlots under 100 acres."
            },
            {
                'NAICS_10_Digit': naics_8 + '02',
                'NAICS_10_Title': f"{title_8} - Medium Forest (100-1000 acres)",
                'Differentiation_Criteria_10': 'Forest Size',
                'Description_10': f"{desc_8} Medium-sized forest holdings 100-1000 acres."
            },
            {
                'NAICS_10_Digit': naics_8 + '03',
                'NAICS_10_Title': f"{title_8} - Large Timberland (1000+ acres)",
                'Differentiation_Criteria_10': 'Forest Size',
                'Description_10': f"{desc_8} Large commercial timberlands over 1000 acres."
            },
            {
                'NAICS_10_Digit': naics_8 + '04',
                'NAICS_10_Title': f"{title_8} - Sustainable/FSC Certified",
                'Differentiation_Criteria_10': 'Certification',
                'Description_10': f"{desc_8} Operations with sustainable forestry certifications (FSC, SFI, etc.)."
            },
            {
                'NAICS_10_Digit': naics_8 + '05',
                'NAICS_10_Title': f"{title_8} - Carbon Credit Focused",
                'Differentiation_Criteria_10': 'Business Model',
                'Description_10': f"{desc_8} Forestry operations participating in carbon credit markets."
            }
        ]

    def generate_fishing_hunting(self, naics_6: str, naics_8: str, title_8: str,
                                 criteria_8: str, desc_8: str) -> List[Dict]:
        """Generate fishing/hunting specific 10-digit codes"""
        title_lower = title_8.lower()

        if 'aquaculture' in title_lower or 'farm' in title_lower:
            # Aquaculture operations
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Small-Scale (<10 acres)",
                    'Differentiation_Criteria_10': 'Operation Size',
                    'Description_10': f"{desc_8} Small aquaculture operations under 10 acres of water surface."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Medium-Scale (10-50 acres)",
                    'Differentiation_Criteria_10': 'Operation Size',
                    'Description_10': f"{desc_8} Medium operations with 10-50 acres of production."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Large Commercial (50+ acres)",
                    'Differentiation_Criteria_10': 'Operation Size',
                    'Description_10': f"{desc_8} Large commercial operations over 50 acres."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Recirculating Aquaculture Systems (RAS)",
                    'Differentiation_Criteria_10': 'Technology',
                    'Description_10': f"{desc_8} Indoor recirculating systems for intensive production."
                },
                {
                    'NAICS_10_Digit': naics_8 + '05',
                    'NAICS_10_Title': f"{title_8} - Organic/Sustainable Certified",
                    'Differentiation_Criteria_10': 'Certification',
                    'Description_10': f"{desc_8} Operations with organic or sustainability certifications."
                }
            ]
        else:
            # Wild catch fishing
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Small Vessel Operations",
                    'Differentiation_Criteria_10': 'Fleet Size',
                    'Description_10': f"{desc_8} Small-scale operations with vessels under 50 feet."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Medium Vessel Fleet",
                    'Differentiation_Criteria_10': 'Fleet Size',
                    'Description_10': f"{desc_8} Medium-sized vessels 50-100 feet."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Large Commercial Fleet",
                    'Differentiation_Criteria_10': 'Fleet Size',
                    'Description_10': f"{desc_8} Large commercial vessels over 100 feet."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Sustainable/MSC Certified",
                    'Differentiation_Criteria_10': 'Certification',
                    'Description_10': f"{desc_8} Operations with Marine Stewardship Council or similar certification."
                }
            ]

    def generate_ag_support(self, naics_6: str, naics_8: str, title_8: str,
                           criteria_8: str, desc_8: str) -> List[Dict]:
        """Generate agricultural support services 10-digit codes"""
        return [
            {
                'NAICS_10_Digit': naics_8 + '01',
                'NAICS_10_Title': f"{title_8} - Small Independent Service",
                'Differentiation_Criteria_10': 'Business Size',
                'Description_10': f"{desc_8} Small independent service providers, often owner-operated."
            },
            {
                'NAICS_10_Digit': naics_8 + '02',
                'NAICS_10_Title': f"{title_8} - Regional Service Provider",
                'Differentiation_Criteria_10': 'Business Size',
                'Description_10': f"{desc_8} Regional companies serving multiple counties or states."
            },
            {
                'NAICS_10_Digit': naics_8 + '03',
                'NAICS_10_Title': f"{title_8} - Technology-Enhanced Services",
                'Differentiation_Criteria_10': 'Technology Level',
                'Description_10': f"{desc_8} Services utilizing GPS, sensors, drones, or precision ag technology."
            },
            {
                'NAICS_10_Digit': naics_8 + '04',
                'NAICS_10_Title': f"{title_8} - Custom/Specialty Services",
                'Differentiation_Criteria_10': 'Service Specialization',
                'Description_10': f"{desc_8} Specialized services for organic, specialty crops, or niche markets."
            }
        ]

    def generate_generic_ag(self, naics_8: str, title_8: str,
                           criteria_8: str, desc_8: str) -> List[Dict]:
        """Generic agricultural extensions"""
        return [
            {
                'NAICS_10_Digit': naics_8 + '01',
                'NAICS_10_Title': f"{title_8} - Small-Scale Operations",
                'Differentiation_Criteria_10': 'Operation Size',
                'Description_10': f"{desc_8} Small family or hobby farm operations."
            },
            {
                'NAICS_10_Digit': naics_8 + '02',
                'NAICS_10_Title': f"{title_8} - Medium Commercial Operations",
                'Differentiation_Criteria_10': 'Operation Size',
                'Description_10': f"{desc_8} Medium-sized commercial operations."
            },
            {
                'NAICS_10_Digit': naics_8 + '03',
                'NAICS_10_Title': f"{title_8} - Large Industrial Operations",
                'Differentiation_Criteria_10': 'Operation Size',
                'Description_10': f"{desc_8} Large industrial-scale operations."
            },
            {
                'NAICS_10_Digit': naics_8 + '04',
                'NAICS_10_Title': f"{title_8} - Sustainable/Certified",
                'Differentiation_Criteria_10': 'Production Method',
                'Description_10': f"{desc_8} Operations with sustainability certifications."
            }
        ]

    # ========== SECTOR 21: MINING, QUARRYING, OIL & GAS EXTRACTION ==========

    def generate_mining(self, naics_6: str, naics_8: str, title_8: str,
                       criteria_8: str, desc_8: str) -> List[Dict]:
        """Mining sector with scale and technology differentiation"""
        title_lower = title_8.lower()

        # Determine type of extraction
        is_oil_gas = any(word in title_lower for word in ['oil', 'gas', 'petroleum', 'natural gas'])
        is_coal = 'coal' in title_lower
        is_metal = any(word in title_lower for word in ['gold', 'silver', 'copper', 'iron', 'metal', 'ore'])
        is_nonmetal = any(word in title_lower for word in ['sand', 'gravel', 'stone', 'quarr', 'limestone', 'granite'])

        if is_oil_gas:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Independent Operators",
                    'Differentiation_Criteria_10': 'Company Type',
                    'Description_10': f"{desc_8} Independent oil and gas producers."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Major Integrated Companies",
                    'Differentiation_Criteria_10': 'Company Type',
                    'Description_10': f"{desc_8} Large integrated energy companies with exploration and production."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Offshore Operations",
                    'Differentiation_Criteria_10': 'Location Type',
                    'Description_10': f"{desc_8} Offshore oil and gas extraction operations."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Onshore Conventional",
                    'Differentiation_Criteria_10': 'Extraction Method',
                    'Description_10': f"{desc_8} Conventional onshore extraction methods."
                },
                {
                    'NAICS_10_Digit': naics_8 + '05',
                    'NAICS_10_Title': f"{title_8} - Hydraulic Fracturing/Shale",
                    'Differentiation_Criteria_10': 'Extraction Method',
                    'Description_10': f"{desc_8} Operations using hydraulic fracturing for shale formations."
                }
            ]
        elif is_coal:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Surface Mining",
                    'Differentiation_Criteria_10': 'Mining Method',
                    'Description_10': f"{desc_8} Surface or open-pit coal mining operations."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Underground Mining",
                    'Differentiation_Criteria_10': 'Mining Method',
                    'Description_10': f"{desc_8} Underground deep coal mining operations."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Small Independent Mines",
                    'Differentiation_Criteria_10': 'Operation Scale',
                    'Description_10': f"{desc_8} Small independent coal mining operations."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Large Commercial Mines",
                    'Differentiation_Criteria_10': 'Operation Scale',
                    'Description_10': f"{desc_8} Large commercial coal mining operations."
                }
            ]
        elif is_metal:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Open-Pit Mining",
                    'Differentiation_Criteria_10': 'Mining Method',
                    'Description_10': f"{desc_8} Open-pit or surface metal ore mining."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Underground Mining",
                    'Differentiation_Criteria_10': 'Mining Method',
                    'Description_10': f"{desc_8} Underground metal ore mining operations."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Junior Mining Companies",
                    'Differentiation_Criteria_10': 'Company Size',
                    'Description_10': f"{desc_8} Junior exploration and small-scale production companies."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Major Mining Operations",
                    'Differentiation_Criteria_10': 'Company Size',
                    'Description_10': f"{desc_8} Large multinational mining corporations."
                }
            ]
        else:  # Non-metallic minerals
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Small Quarry (<50K tons/year)",
                    'Differentiation_Criteria_10': 'Production Volume',
                    'Description_10': f"{desc_8} Small operations producing under 50,000 tons annually."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Medium Operation (50K-500K tons/year)",
                    'Differentiation_Criteria_10': 'Production Volume',
                    'Description_10': f"{desc_8} Medium operations producing 50,000-500,000 tons annually."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Large Quarry (500K+ tons/year)",
                    'Differentiation_Criteria_10': 'Production Volume',
                    'Description_10': f"{desc_8} Large operations producing over 500,000 tons annually."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Mobile/Portable Operations",
                    'Differentiation_Criteria_10': 'Operation Type',
                    'Description_10': f"{desc_8} Mobile crushing and screening operations."
                }
            ]

    # ========== SECTOR 22: UTILITIES ==========

    def generate_utilities(self, naics_6: str, naics_8: str, title_8: str,
                          criteria_8: str, desc_8: str) -> List[Dict]:
        """Utilities sector with generation and distribution differentiation"""
        title_lower = title_8.lower()

        is_electric = 'electric' in title_lower or 'power' in title_lower
        is_gas = 'gas' in title_lower and 'natural' in title_lower
        is_water = 'water' in title_lower or 'sewer' in title_lower
        is_renewable = any(word in title_lower for word in ['solar', 'wind', 'hydro', 'renewable', 'geothermal'])

        if is_renewable:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Small Distributed (<10 MW)",
                    'Differentiation_Criteria_10': 'Generation Capacity',
                    'Description_10': f"{desc_8} Small distributed renewable generation under 10 megawatts."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Medium Scale (10-100 MW)",
                    'Differentiation_Criteria_10': 'Generation Capacity',
                    'Description_10': f"{desc_8} Medium-scale renewable generation 10-100 megawatts."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Utility Scale (100+ MW)",
                    'Differentiation_Criteria_10': 'Generation Capacity',
                    'Description_10': f"{desc_8} Large utility-scale renewable generation over 100 megawatts."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Independent Power Producer",
                    'Differentiation_Criteria_10': 'Business Model',
                    'Description_10': f"{desc_8} Independent renewable energy producers selling to grid."
                }
            ]
        elif is_electric:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Municipal Utility",
                    'Differentiation_Criteria_10': 'Ownership Type',
                    'Description_10': f"{desc_8} Municipally-owned and operated electric utilities."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Investor-Owned Utility",
                    'Differentiation_Criteria_10': 'Ownership Type',
                    'Description_10': f"{desc_8} Investor-owned electric utilities serving large regions."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Rural Electric Cooperative",
                    'Differentiation_Criteria_10': 'Ownership Type',
                    'Description_10': f"{desc_8} Member-owned rural electric cooperatives."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Transmission Only",
                    'Differentiation_Criteria_10': 'Service Type',
                    'Description_10': f"{desc_8} Companies focused on high-voltage transmission infrastructure."
                },
                {
                    'NAICS_10_Digit': naics_8 + '05',
                    'NAICS_10_Title': f"{title_8} - Distribution Only",
                    'Differentiation_Criteria_10': 'Service Type',
                    'Description_10': f"{desc_8} Local distribution companies delivering to end users."
                }
            ]
        elif is_gas:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Local Distribution Company",
                    'Differentiation_Criteria_10': 'Service Type',
                    'Description_10': f"{desc_8} Local natural gas distribution to residential and commercial customers."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Interstate Pipeline",
                    'Differentiation_Criteria_10': 'Service Type',
                    'Description_10': f"{desc_8} Interstate natural gas pipeline transmission companies."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Municipal Gas System",
                    'Differentiation_Criteria_10': 'Ownership Type',
                    'Description_10': f"{desc_8} Municipally-owned natural gas systems."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Investor-Owned System",
                    'Differentiation_Criteria_10': 'Ownership Type',
                    'Description_10': f"{desc_8} Investor-owned natural gas utilities."
                }
            ]
        elif is_water:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Small System (<3,300 population)",
                    'Differentiation_Criteria_10': 'System Size',
                    'Description_10': f"{desc_8} Small water/sewer systems serving under 3,300 people."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Medium System (3,300-50,000 population)",
                    'Differentiation_Criteria_10': 'System Size',
                    'Description_10': f"{desc_8} Medium systems serving 3,300-50,000 people."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Large System (50,000+ population)",
                    'Differentiation_Criteria_10': 'System Size',
                    'Description_10': f"{desc_8} Large systems serving over 50,000 people."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Private Utility Company",
                    'Differentiation_Criteria_10': 'Ownership Type',
                    'Description_10': f"{desc_8} Privately-owned water/sewer utilities."
                }
            ]
        else:
            return self.generate_generic(naics_8, title_8, criteria_8, desc_8)

    # ========== SECTOR 23: CONSTRUCTION ==========

    def generate_construction(self, naics_6: str, naics_8: str, title_8: str,
                             criteria_8: str, desc_8: str) -> List[Dict]:
        """Construction sector with company size and project type differentiation"""
        title_lower = title_8.lower()

        # Residential building construction
        is_residential = any(word in title_lower for word in [
            'residential', 'home', 'house', 'housing', 'single-family', 'multi-family',
            'apartment', 'townhome', 'condominium', 'spec home', 'custom home', 'modular home',
            'remodeling', 'remodel', 'renovation', 'restoration', 'addition', 'basement finishing'
        ])

        # Commercial and institutional construction
        is_commercial = any(word in title_lower for word in [
            'commercial', 'office building', 'retail center', 'hotel', 'hospitality',
            'healthcare facility', 'hospital', 'medical', 'educational facility', 'school',
            'religious building', 'restaurant construction', 'institutional'
        ])

        # Industrial construction
        is_industrial = any(word in title_lower for word in [
            'manufacturing plant', 'warehouse', 'distribution center', 'food processing plant',
            'data center', 'cold storage', 'industrial building', 'plant construction', 'factory'
        ])

        # Specialty trade contractors
        is_specialty = any(word in title_lower for word in [
            'electrical', 'plumbing', 'hvac', 'heating', 'air-conditioning', 'roofing',
            'concrete', 'framing', 'masonry', 'painting', 'drywall', 'insulation', 'siding',
            'flooring', 'tile', 'terrazzo', 'glass', 'glazing', 'finish carpentry'
        ])

        # Heavy and civil engineering construction
        is_heavy = any(word in title_lower for word in [
            'highway', 'street', 'bridge', 'road', 'pipeline', 'utility', 'infrastructure',
            'heavy', 'water main', 'sewer', 'wastewater', 'water treatment',
            'transmission line', 'substation', 'power line', 'communication line'
        ])

        # Land subdivision and site prep
        is_site_prep = any(word in title_lower for word in [
            'site preparation', 'land subdivision', 'grading', 'excavation'
        ])

        # Check industrial/commercial/heavy first, then residential to avoid 'warehouse' containing 'house'
        if is_industrial:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Small Projects (<$10M)",
                    'Differentiation_Criteria_10': 'Project Size',
                    'Description_10': f"{desc_8} Small industrial construction projects under $10 million."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Medium Projects ($10M-$100M)",
                    'Differentiation_Criteria_10': 'Project Size',
                    'Description_10': f"{desc_8} Medium industrial projects $10-100 million."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Large Projects ($100M+)",
                    'Differentiation_Criteria_10': 'Project Size',
                    'Description_10': f"{desc_8} Major industrial construction over $100 million."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Process/Specialty Construction",
                    'Differentiation_Criteria_10': 'Specialization',
                    'Description_10': f"{desc_8} Specialized process and technical industrial construction."
                }
            ]
        elif is_commercial:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Small Projects (<$5M)",
                    'Differentiation_Criteria_10': 'Project Size',
                    'Description_10': f"{desc_8} Contractors handling projects under $5 million."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Medium Projects ($5M-$50M)",
                    'Differentiation_Criteria_10': 'Project Size',
                    'Description_10': f"{desc_8} Contractors for projects $5-50 million."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Large Projects ($50M+)",
                    'Differentiation_Criteria_10': 'Project Size',
                    'Description_10': f"{desc_8} Major contractors for projects over $50 million."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Design-Build Contractor",
                    'Differentiation_Criteria_10': 'Delivery Method',
                    'Description_10': f"{desc_8} Design-build integrated project delivery."
                },
                {
                    'NAICS_10_Digit': naics_8 + '05',
                    'NAICS_10_Title': f"{title_8} - Construction Management",
                    'Differentiation_Criteria_10': 'Delivery Method',
                    'Description_10': f"{desc_8} Construction management and general contracting services."
                }
            ]
        elif is_specialty:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Small Contractor (1-10 employees)",
                    'Differentiation_Criteria_10': 'Company Size',
                    'Description_10': f"{desc_8} Small specialty contractors with 1-10 employees."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Medium Contractor (10-50 employees)",
                    'Differentiation_Criteria_10': 'Company Size',
                    'Description_10': f"{desc_8} Medium contractors with 10-50 employees."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Large Contractor (50+ employees)",
                    'Differentiation_Criteria_10': 'Company Size',
                    'Description_10': f"{desc_8} Large specialty contractors with over 50 employees."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Residential Focus",
                    'Differentiation_Criteria_10': 'Market Focus',
                    'Description_10': f"{desc_8} Contractors focused primarily on residential projects."
                },
                {
                    'NAICS_10_Digit': naics_8 + '05',
                    'NAICS_10_Title': f"{title_8} - Commercial/Industrial Focus",
                    'Differentiation_Criteria_10': 'Market Focus',
                    'Description_10': f"{desc_8} Contractors focused on commercial and industrial projects."
                }
            ]
        elif is_residential and not is_specialty:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Small Builder (1-10 homes/year)",
                    'Differentiation_Criteria_10': 'Production Volume',
                    'Description_10': f"{desc_8} Small custom home builders producing 1-10 homes annually."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Medium Builder (10-100 homes/year)",
                    'Differentiation_Criteria_10': 'Production Volume',
                    'Description_10': f"{desc_8} Medium builders producing 10-100 homes annually."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Large Production Builder (100+ homes/year)",
                    'Differentiation_Criteria_10': 'Production Volume',
                    'Description_10': f"{desc_8} Large production builders with over 100 homes annually."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Custom/Luxury Builder",
                    'Differentiation_Criteria_10': 'Market Segment',
                    'Description_10': f"{desc_8} Custom and luxury home builders serving premium market."
                },
                {
                    'NAICS_10_Digit': naics_8 + '05',
                    'NAICS_10_Title': f"{title_8} - Green/Sustainable Building",
                    'Differentiation_Criteria_10': 'Specialization',
                    'Description_10': f"{desc_8} Builders specializing in green, sustainable, or net-zero homes."
                }
            ]
        elif is_heavy:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Regional Contractor",
                    'Differentiation_Criteria_10': 'Geographic Scope',
                    'Description_10': f"{desc_8} Regional heavy construction contractors."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - National Contractor",
                    'Differentiation_Criteria_10': 'Geographic Scope',
                    'Description_10': f"{desc_8} National heavy construction firms."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Public Works Specialist",
                    'Differentiation_Criteria_10': 'Client Type',
                    'Description_10': f"{desc_8} Specialists in government and public works projects."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Private Sector Projects",
                    'Differentiation_Criteria_10': 'Client Type',
                    'Description_10': f"{desc_8} Focus on private sector heavy construction."
                }
            ]
        elif is_site_prep:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Small Contractor (1-5 equipment)",
                    'Differentiation_Criteria_10': 'Company Size',
                    'Description_10': f"{desc_8} Small contractors with 1-5 pieces of equipment."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Medium Contractor (6-20 equipment)",
                    'Differentiation_Criteria_10': 'Company Size',
                    'Description_10': f"{desc_8} Medium contractors with 6-20 pieces of equipment."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Large Contractor (21+ equipment)",
                    'Differentiation_Criteria_10': 'Company Size',
                    'Description_10': f"{desc_8} Large contractors with over 20 pieces of equipment."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Residential Development Focus",
                    'Differentiation_Criteria_10': 'Market Focus',
                    'Description_10': f"{desc_8} Contractors focused on residential development projects."
                }
            ]
        else:
            return self.generate_generic(naics_8, title_8, criteria_8, desc_8)

    # ========== SECTORS 31-33: MANUFACTURING ==========

    def generate_manufacturing(self, naics_6: str, naics_8: str, title_8: str,
                              criteria_8: str, desc_8: str) -> List[Dict]:
        """Manufacturing sectors with production scale and automation differentiation"""
        title_lower = title_8.lower()

        # Key dimensions for manufacturing:
        # - Production volume/scale
        # - Automation level
        # - Market segment (OEM, aftermarket, industrial, consumer)
        # - Business model (job shop, batch, continuous, custom)

        is_food = any(word in title_lower for word in ['food', 'beverage', 'bakery', 'dairy', 'meat', 'fruit', 'vegetable'])
        is_custom = any(word in title_lower for word in ['custom', 'job shop', 'specialty', 'artisan', 'craft'])
        is_tech = any(word in title_lower for word in ['electronic', 'semiconductor', 'computer', 'software', 'circuit'])
        is_machinery = any(word in title_lower for word in ['machinery', 'equipment', 'tool', 'engine'])
        is_chemical = any(word in title_lower for word in ['chemical', 'pharmaceutical', 'drug', 'medicine'])

        if is_food:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Artisan/Small Batch",
                    'Differentiation_Criteria_10': 'Production Scale',
                    'Description_10': f"{desc_8} Small artisan or craft producers with batch production."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Regional Production",
                    'Differentiation_Criteria_10': 'Production Scale',
                    'Description_10': f"{desc_8} Regional manufacturers with multi-state distribution."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - National/Mass Production",
                    'Differentiation_Criteria_10': 'Production Scale',
                    'Description_10': f"{desc_8} Large national manufacturers with mass production."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Private Label/Co-Packer",
                    'Differentiation_Criteria_10': 'Business Model',
                    'Description_10': f"{desc_8} Contract manufacturers and private label producers."
                },
                {
                    'NAICS_10_Digit': naics_8 + '05',
                    'NAICS_10_Title': f"{title_8} - Organic/Premium Certified",
                    'Differentiation_Criteria_10': 'Product Positioning',
                    'Description_10': f"{desc_8} Certified organic or premium product manufacturers."
                }
            ]
        elif is_tech:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Prototype/Low Volume",
                    'Differentiation_Criteria_10': 'Production Volume',
                    'Description_10': f"{desc_8} Prototype and low-volume specialized production."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Medium Volume Production",
                    'Differentiation_Criteria_10': 'Production Volume',
                    'Description_10': f"{desc_8} Medium-volume production for niche markets."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - High Volume/Mass Production",
                    'Differentiation_Criteria_10': 'Production Volume',
                    'Description_10': f"{desc_8} High-volume automated mass production."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Contract Manufacturing (CM/EMS)",
                    'Differentiation_Criteria_10': 'Business Model',
                    'Description_10': f"{desc_8} Contract manufacturers and electronics manufacturing services."
                },
                {
                    'NAICS_10_Digit': naics_8 + '05',
                    'NAICS_10_Title': f"{title_8} - Vertically Integrated OEM",
                    'Differentiation_Criteria_10': 'Business Model',
                    'Description_10': f"{desc_8} Vertically integrated original equipment manufacturers."
                }
            ]
        elif is_machinery:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Custom/Engineered Solutions",
                    'Differentiation_Criteria_10': 'Production Type',
                    'Description_10': f"{desc_8} Custom-engineered machinery for specific applications."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Standard Product Lines",
                    'Differentiation_Criteria_10': 'Production Type',
                    'Description_10': f"{desc_8} Standardized machinery product lines with options."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - OEM Component Supplier",
                    'Differentiation_Criteria_10': 'Market Channel',
                    'Description_10': f"{desc_8} Component suppliers to OEM machinery manufacturers."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Aftermarket/Replacement Parts",
                    'Differentiation_Criteria_10': 'Market Channel',
                    'Description_10': f"{desc_8} Aftermarket and replacement parts manufacturers."
                }
            ]
        elif is_chemical:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Research/Specialty Chemicals",
                    'Differentiation_Criteria_10': 'Product Type',
                    'Description_10': f"{desc_8} Specialty and research-grade chemical production."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Commodity/Bulk Production",
                    'Differentiation_Criteria_10': 'Product Type',
                    'Description_10': f"{desc_8} Large-scale commodity chemical production."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Pharmaceutical Grade (GMP)",
                    'Differentiation_Criteria_10': 'Quality Standard',
                    'Description_10': f"{desc_8} GMP-certified pharmaceutical-grade manufacturing."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Custom Synthesis/Contract",
                    'Differentiation_Criteria_10': 'Business Model',
                    'Description_10': f"{desc_8} Custom chemical synthesis and contract manufacturing."
                }
            ]
        else:
            # General manufacturing differentiation
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Small Manufacturer (<50 employees)",
                    'Differentiation_Criteria_10': 'Company Size',
                    'Description_10': f"{desc_8} Small manufacturers with fewer than 50 employees."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Medium Manufacturer (50-500 employees)",
                    'Differentiation_Criteria_10': 'Company Size',
                    'Description_10': f"{desc_8} Medium-sized manufacturers with 50-500 employees."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Large Manufacturer (500+ employees)",
                    'Differentiation_Criteria_10': 'Company Size',
                    'Description_10': f"{desc_8} Large manufacturers with over 500 employees."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Automated/Industry 4.0",
                    'Differentiation_Criteria_10': 'Technology Level',
                    'Description_10': f"{desc_8} Highly automated facilities with Industry 4.0 technologies."
                },
                {
                    'NAICS_10_Digit': naics_8 + '05',
                    'NAICS_10_Title': f"{title_8} - Job Shop/Custom Production",
                    'Differentiation_Criteria_10': 'Production Type',
                    'Description_10': f"{desc_8} Job shop operations specializing in custom production."
                }
            ]

    # ========== SECTOR 42: WHOLESALE TRADE ==========

    def generate_wholesale(self, naics_6: str, naics_8: str, title_8: str,
                          criteria_8: str, desc_8: str) -> List[Dict]:
        """Wholesale trade with distributor type and coverage differentiation"""
        return [
            {
                'NAICS_10_Digit': naics_8 + '01',
                'NAICS_10_Title': f"{title_8} - Local/Regional Distributor",
                'Differentiation_Criteria_10': 'Geographic Scope',
                'Description_10': f"{desc_8} Local or regional wholesalers serving limited geographic area."
            },
            {
                'NAICS_10_Digit': naics_8 + '02',
                'NAICS_10_Title': f"{title_8} - National Distributor",
                'Differentiation_Criteria_10': 'Geographic Scope',
                'Description_10': f"{desc_8} National wholesalers with multi-state or nationwide distribution."
            },
            {
                'NAICS_10_Digit': naics_8 + '03',
                'NAICS_10_Title': f"{title_8} - Import/Export Specialist",
                'Differentiation_Criteria_10': 'Business Model',
                'Description_10': f"{desc_8} Wholesalers specializing in international import/export trade."
            },
            {
                'NAICS_10_Digit': naics_8 + '04',
                'NAICS_10_Title': f"{title_8} - Drop Shipper/Broker",
                'Differentiation_Criteria_10': 'Business Model',
                'Description_10': f"{desc_8} Drop shipping and brokerage without inventory holding."
            },
            {
                'NAICS_10_Digit': naics_8 + '05',
                'NAICS_10_Title': f"{title_8} - Value-Added Distributor",
                'Differentiation_Criteria_10': 'Service Level',
                'Description_10': f"{desc_8} Distributors providing assembly, kitting, or technical services."
            }
        ]

    # ========== SECTORS 44-45: RETAIL TRADE ==========

    def generate_retail(self, naics_6: str, naics_8: str, title_8: str,
                       criteria_8: str, desc_8: str) -> List[Dict]:
        """Retail trade with store format and channel differentiation"""
        title_lower = title_8.lower()

        is_specialty = any(word in title_lower for word in ['specialty', 'boutique', 'custom'])
        is_online = any(word in title_lower for word in ['online', 'e-commerce', 'internet', 'electronic'])

        if is_online:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Pure-Play E-commerce",
                    'Differentiation_Criteria_10': 'Channel Strategy',
                    'Description_10': f"{desc_8} Online-only retailers without physical stores."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Omnichannel with Stores",
                    'Differentiation_Criteria_10': 'Channel Strategy',
                    'Description_10': f"{desc_8} Online retailers with integrated physical store presence."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Marketplace Platform",
                    'Differentiation_Criteria_10': 'Business Model',
                    'Description_10': f"{desc_8} Online marketplace platforms connecting third-party sellers."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Direct-to-Consumer Brand",
                    'Differentiation_Criteria_10': 'Business Model',
                    'Description_10': f"{desc_8} Manufacturer direct-to-consumer online sales."
                }
            ]
        else:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Independent Single Store",
                    'Differentiation_Criteria_10': 'Store Format',
                    'Description_10': f"{desc_8} Independent retailers with single location."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Small Chain (2-10 stores)",
                    'Differentiation_Criteria_10': 'Store Format',
                    'Description_10': f"{desc_8} Small retail chains with 2-10 locations."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Regional Chain (11-100 stores)",
                    'Differentiation_Criteria_10': 'Store Format',
                    'Description_10': f"{desc_8} Regional chains with 11-100 store locations."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - National Chain (100+ stores)",
                    'Differentiation_Criteria_10': 'Store Format',
                    'Description_10': f"{desc_8} National retail chains with over 100 locations."
                },
                {
                    'NAICS_10_Digit': naics_8 + '05',
                    'NAICS_10_Title': f"{title_8} - Franchise Operation",
                    'Differentiation_Criteria_10': 'Business Model',
                    'Description_10': f"{desc_8} Franchise-operated retail locations."
                }
            ]

    # ========== SECTORS 48-49: TRANSPORTATION & WAREHOUSING ==========

    def generate_transportation(self, naics_6: str, naics_8: str, title_8: str,
                               criteria_8: str, desc_8: str) -> List[Dict]:
        """Transportation with fleet size and service type differentiation"""
        title_lower = title_8.lower()

        # Sector 49 - Warehousing and Courier/Delivery services
        is_courier = any(word in title_lower for word in ['courier', 'delivery', 'messenger', 'postal', 'package', 'parcel', 'express'])
        is_warehousing = any(word in title_lower for word in ['warehouse', 'warehousing', 'storage', 'distribution center', 'fulfillment'])

        # Sector 48 - Transportation modes
        is_trucking = any(word in title_lower for word in ['truck', 'freight', 'cargo', 'moving', 'van line', 'hauling'])
        is_passenger = any(word in title_lower for word in ['passenger', 'transit', 'bus', 'taxi', 'ride', 'limousine', 'shuttle', 'charter'])
        is_air = any(word in title_lower for word in ['air', 'aviation', 'airline', 'aircraft'])
        is_water = any(word in title_lower for word in ['water', 'marine', 'ship', 'vessel', 'ferry', 'cruise', 'barge'])
        is_rail = any(word in title_lower for word in ['rail', 'train', 'railroad', 'locomotive'])
        is_pipeline = 'pipeline' in title_lower
        is_ambulance = 'ambulance' in title_lower

        # Courier and express delivery (Sector 49)
        if is_courier:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Local/Same-Day Service",
                    'Differentiation_Criteria_10': 'Service Scope',
                    'Description_10': f"{desc_8} Local and same-day delivery within metropolitan areas."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Regional Network",
                    'Differentiation_Criteria_10': 'Service Scope',
                    'Description_10': f"{desc_8} Regional delivery network covering multiple cities or states."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - National Integrated Service",
                    'Differentiation_Criteria_10': 'Service Scope',
                    'Description_10': f"{desc_8} National courier and delivery network with integrated logistics."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - International/Global Express",
                    'Differentiation_Criteria_10': 'Service Scope',
                    'Description_10': f"{desc_8} International and global express delivery services."
                },
                {
                    'NAICS_10_Digit': naics_8 + '05',
                    'NAICS_10_Title': f"{title_8} - On-Demand/Gig Platform",
                    'Differentiation_Criteria_10': 'Business Model',
                    'Description_10': f"{desc_8} Technology-enabled on-demand delivery platforms using gig workers."
                }
            ]
        # Warehousing and storage (Sector 49)
        elif is_warehousing:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Small Facility (<50K sq ft)",
                    'Differentiation_Criteria_10': 'Facility Size',
                    'Description_10': f"{desc_8} Small warehouses and storage facilities under 50,000 square feet."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Medium Facility (50K-200K sq ft)",
                    'Differentiation_Criteria_10': 'Facility Size',
                    'Description_10': f"{desc_8} Medium distribution centers 50,000-200,000 square feet."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Large Facility (200K+ sq ft)",
                    'Differentiation_Criteria_10': 'Facility Size',
                    'Description_10': f"{desc_8} Large regional distribution centers over 200,000 square feet."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Automated/Robotic Systems",
                    'Differentiation_Criteria_10': 'Technology Level',
                    'Description_10': f"{desc_8} Automated warehouses with robotics, AS/RS, and advanced WMS."
                },
                {
                    'NAICS_10_Digit': naics_8 + '05',
                    'NAICS_10_Title': f"{title_8} - 3PL/Fulfillment Centers",
                    'Differentiation_Criteria_10': 'Service Model',
                    'Description_10': f"{desc_8} Third-party logistics and e-commerce fulfillment centers."
                }
            ]
        # Trucking and freight (Sector 48)
        elif is_trucking:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Owner-Operator (1-5 trucks)",
                    'Differentiation_Criteria_10': 'Fleet Size',
                    'Description_10': f"{desc_8} Owner-operators and small carriers with 1-5 trucks."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Small Carrier (6-50 trucks)",
                    'Differentiation_Criteria_10': 'Fleet Size',
                    'Description_10': f"{desc_8} Small trucking companies with 6-50 trucks."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Medium Carrier (51-500 trucks)",
                    'Differentiation_Criteria_10': 'Fleet Size',
                    'Description_10': f"{desc_8} Medium carriers with 51-500 trucks."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Large Carrier (500+ trucks)",
                    'Differentiation_Criteria_10': 'Fleet Size',
                    'Description_10': f"{desc_8} Large national carriers with over 500 trucks."
                },
                {
                    'NAICS_10_Digit': naics_8 + '05',
                    'NAICS_10_Title': f"{title_8} - Dedicated Contract Carriage",
                    'Differentiation_Criteria_10': 'Business Model',
                    'Description_10': f"{desc_8} Dedicated contract carriage for specific shippers."
                }
            ]
        # Passenger transportation (Sector 48)
        elif is_passenger:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Small Operation (<10 vehicles)",
                    'Differentiation_Criteria_10': 'Fleet Size',
                    'Description_10': f"{desc_8} Small passenger services with under 10 vehicles."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Medium Fleet (10-50 vehicles)",
                    'Differentiation_Criteria_10': 'Fleet Size',
                    'Description_10': f"{desc_8} Medium operations with 10-50 vehicles."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Large Fleet (50+ vehicles)",
                    'Differentiation_Criteria_10': 'Fleet Size',
                    'Description_10': f"{desc_8} Large passenger services with over 50 vehicles."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - On-Demand/App-Based",
                    'Differentiation_Criteria_10': 'Service Model',
                    'Description_10': f"{desc_8} Technology-enabled on-demand ride services."
                },
                {
                    'NAICS_10_Digit': naics_8 + '05',
                    'NAICS_10_Title': f"{title_8} - Premium/Luxury Service",
                    'Differentiation_Criteria_10': 'Service Level',
                    'Description_10': f"{desc_8} Premium and luxury passenger transportation."
                }
            ]
        # Air transportation (Sector 48)
        elif is_air:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Small/Regional Operator",
                    'Differentiation_Criteria_10': 'Operation Scale',
                    'Description_10': f"{desc_8} Small and regional air service operators."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - National Carrier",
                    'Differentiation_Criteria_10': 'Operation Scale',
                    'Description_10': f"{desc_8} National air transportation carriers."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - International/Global Network",
                    'Differentiation_Criteria_10': 'Operation Scale',
                    'Description_10': f"{desc_8} International airlines with global route networks."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Charter/On-Demand",
                    'Differentiation_Criteria_10': 'Service Model',
                    'Description_10': f"{desc_8} Charter and on-demand air transportation services."
                }
            ]
        # Water transportation (Sector 48)
        elif is_water:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Small Vessel Operation",
                    'Differentiation_Criteria_10': 'Fleet Size',
                    'Description_10': f"{desc_8} Small vessel operations with limited fleet."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Regional Service",
                    'Differentiation_Criteria_10': 'Service Scope',
                    'Description_10': f"{desc_8} Regional water transportation services."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Oceangoing Fleet",
                    'Differentiation_Criteria_10': 'Service Scope',
                    'Description_10': f"{desc_8} Oceangoing vessels for international shipping."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Specialized Cargo",
                    'Differentiation_Criteria_10': 'Service Type',
                    'Description_10': f"{desc_8} Specialized cargo vessels (tankers, container, bulk)."
                }
            ]
        # Ambulance services (healthcare transportation)
        elif is_ambulance:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Basic Life Support (BLS)",
                    'Differentiation_Criteria_10': 'Service Level',
                    'Description_10': f"{desc_8} Basic life support ambulance services."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Advanced Life Support (ALS)",
                    'Differentiation_Criteria_10': 'Service Level',
                    'Description_10': f"{desc_8} Advanced life support paramedic ambulance services."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Critical Care Transport",
                    'Differentiation_Criteria_10': 'Service Level',
                    'Description_10': f"{desc_8} Critical care inter-facility transport services."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Non-Emergency Medical Transport",
                    'Differentiation_Criteria_10': 'Service Type',
                    'Description_10': f"{desc_8} Non-emergency medical transportation services."
                }
            ]
        else:
            return self.generate_generic(naics_8, title_8, criteria_8, desc_8)

    # ========== SECTOR 51: INFORMATION ==========

    def generate_information(self, naics_6: str, naics_8: str, title_8: str,
                            criteria_8: str, desc_8: str) -> List[Dict]:
        """Information sector with platform and content type differentiation"""
        title_lower = title_8.lower()

        # Publishing
        is_publishing = any(word in title_lower for word in [
            'newspaper', 'magazine', 'periodical', 'book', 'publisher', 'publishing',
            'directory', 'mailing list', 'greeting card', 'calendar', 'map', 'atlas'
        ])

        # Software
        is_software = any(word in title_lower for word in ['software', 'saas', 'application', 'app', 'platform'])

        # Motion picture and video
        is_motion_picture = any(word in title_lower for word in [
            'film', 'movie', 'video', 'cinema', 'theater', 'theatre', 'production',
            'documentary', 'animation', 'vfx', 'visual effects', 'streaming content',
            'distribution', 'editing', 'post-production', 'color grading', 'cgi'
        ])

        # Sound recording
        is_sound_recording = any(word in title_lower for word in [
            'recording studio', 'record label', 'music production', 'music publishing',
            'mastering', 'audio post', 'audio mixing', 'music licensing', 'podcast studio'
        ])

        # Broadcasting and content networks
        is_broadcasting = any(word in title_lower for word in [
            'broadcast', 'radio', 'television', 'tv station', 'cable network',
            'tv network', 'programming network'
        ])

        # Telecommunications
        is_telecom = any(word in title_lower for word in [
            'telecom', 'wireless', 'carrier', 'mvno', 'fiber optic', 'dsl',
            'voip', 'satellite phone', 'long distance', '5g network'
        ])

        # Internet service and cable providers
        is_internet_cable = any(word in title_lower for word in [
            'cable internet', 'internet provider', 'isp', 'satellite internet',
            'satellite tv', 'fixed wireless internet'
        ])

        # Data processing, hosting, and cloud
        is_data_processing = any(word in title_lower for word in [
            'cloud', 'hosting', 'data center', 'colocation', 'managed service',
            'data processing', 'backup', 'disaster recovery', 'cdn', 'content delivery'
        ])

        # Web portals, search engines, social media
        is_web_platform = any(word in title_lower for word in [
            'web portal', 'search engine', 'social media', 'social network',
            'news aggregator', 'web search', 'internet portal'
        ])

        # Libraries and archives
        is_library = any(word in title_lower for word in [
            'library', 'archive', 'stock footage', 'rights management'
        ])

        # Check software FIRST before publishing to avoid "Software Publishers" being caught by 'publisher' keyword
        if is_software:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Startup/Early Stage",
                    'Differentiation_Criteria_10': 'Company Maturity',
                    'Description_10': f"{desc_8} Startup and early-stage software companies."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Growth Stage",
                    'Differentiation_Criteria_10': 'Company Maturity',
                    'Description_10': f"{desc_8} Growth-stage software companies scaling operations."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Enterprise/Established",
                    'Differentiation_Criteria_10': 'Company Maturity',
                    'Description_10': f"{desc_8} Established enterprise software companies."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Open Source/Community",
                    'Differentiation_Criteria_10': 'Business Model',
                    'Description_10': f"{desc_8} Open source software with community or support-based revenue."
                }
            ]
        elif is_publishing:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Small Independent Publisher",
                    'Differentiation_Criteria_10': 'Company Size',
                    'Description_10': f"{desc_8} Small independent publishing operations."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Regional Publisher",
                    'Differentiation_Criteria_10': 'Company Size',
                    'Description_10': f"{desc_8} Regional publishers with multi-market presence."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - National/Major Publisher",
                    'Differentiation_Criteria_10': 'Company Size',
                    'Description_10': f"{desc_8} National and major publishing houses."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Digital-First Publisher",
                    'Differentiation_Criteria_10': 'Business Model',
                    'Description_10': f"{desc_8} Digital-first and online publishing platforms."
                }
            ]
        elif is_motion_picture:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Independent/Boutique",
                    'Differentiation_Criteria_10': 'Company Size',
                    'Description_10': f"{desc_8} Independent and boutique production companies."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Mid-Size Studio",
                    'Differentiation_Criteria_10': 'Company Size',
                    'Description_10': f"{desc_8} Mid-size production studios and companies."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Major Studio/Network",
                    'Differentiation_Criteria_10': 'Company Size',
                    'Description_10': f"{desc_8} Major studios and production networks."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Streaming Platform",
                    'Differentiation_Criteria_10': 'Distribution Model',
                    'Description_10': f"{desc_8} Streaming platform original content production."
                }
            ]
        elif is_sound_recording:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Independent/Project Studio",
                    'Differentiation_Criteria_10': 'Facility Size',
                    'Description_10': f"{desc_8} Independent and project-based studios."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Professional/Commercial Studio",
                    'Differentiation_Criteria_10': 'Facility Size',
                    'Description_10': f"{desc_8} Professional commercial recording facilities."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Major Label/Studio Complex",
                    'Differentiation_Criteria_10': 'Facility Size',
                    'Description_10': f"{desc_8} Major label studios and large facility complexes."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Digital/Virtual Studio",
                    'Differentiation_Criteria_10': 'Technology Level',
                    'Description_10': f"{desc_8} Digital-first and virtual recording operations."
                }
            ]
        elif is_broadcasting:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Local Station",
                    'Differentiation_Criteria_10': 'Coverage Area',
                    'Description_10': f"{desc_8} Local broadcast stations and markets."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Regional Network",
                    'Differentiation_Criteria_10': 'Coverage Area',
                    'Description_10': f"{desc_8} Regional broadcasting networks."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - National Network",
                    'Differentiation_Criteria_10': 'Coverage Area',
                    'Description_10': f"{desc_8} National broadcasting networks."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Digital/Streaming Broadcaster",
                    'Differentiation_Criteria_10': 'Distribution Model',
                    'Description_10': f"{desc_8} Digital streaming and internet broadcasting."
                }
            ]
        elif is_telecom:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Local/Regional Provider",
                    'Differentiation_Criteria_10': 'Coverage Area',
                    'Description_10': f"{desc_8} Local or regional telecommunications providers."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - National Carrier",
                    'Differentiation_Criteria_10': 'Coverage Area',
                    'Description_10': f"{desc_8} National telecommunications carriers."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - MVNO/Reseller",
                    'Differentiation_Criteria_10': 'Business Model',
                    'Description_10': f"{desc_8} Mobile virtual network operators and resellers."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Next-Gen/5G Provider",
                    'Differentiation_Criteria_10': 'Technology Level',
                    'Description_10': f"{desc_8} Next-generation and advanced network providers."
                }
            ]
        elif is_internet_cable:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Local/Regional Provider",
                    'Differentiation_Criteria_10': 'Service Area',
                    'Description_10': f"{desc_8} Local and regional internet/cable providers."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - National Provider",
                    'Differentiation_Criteria_10': 'Service Area',
                    'Description_10': f"{desc_8} National internet and cable service providers."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Reseller/MVNO",
                    'Differentiation_Criteria_10': 'Business Model',
                    'Description_10': f"{desc_8} Resellers and virtual operators."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Fixed Wireless/Satellite",
                    'Differentiation_Criteria_10': 'Technology Type',
                    'Description_10': f"{desc_8} Fixed wireless and satellite service providers."
                }
            ]
        elif is_data_processing:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Small/Boutique Provider",
                    'Differentiation_Criteria_10': 'Company Size',
                    'Description_10': f"{desc_8} Small and boutique service providers."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Regional Provider",
                    'Differentiation_Criteria_10': 'Company Size',
                    'Description_10': f"{desc_8} Regional data center and hosting providers."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - National Provider",
                    'Differentiation_Criteria_10': 'Company Size',
                    'Description_10': f"{desc_8} National-scale providers and data center operators."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Hyperscale/Cloud Giant",
                    'Differentiation_Criteria_10': 'Company Size',
                    'Description_10': f"{desc_8} Hyperscale cloud providers and global operators."
                }
            ]
        elif is_web_platform:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Startup/Emerging Platform",
                    'Differentiation_Criteria_10': 'Platform Maturity',
                    'Description_10': f"{desc_8} Startup and emerging web platforms."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Growth Stage Platform",
                    'Differentiation_Criteria_10': 'Platform Maturity',
                    'Description_10': f"{desc_8} Growth-stage platforms scaling user base."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Established Platform",
                    'Differentiation_Criteria_10': 'Platform Maturity',
                    'Description_10': f"{desc_8} Established platforms with significant market share."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Dominant/Mega Platform",
                    'Differentiation_Criteria_10': 'Platform Maturity',
                    'Description_10': f"{desc_8} Dominant platforms and mega-scale operations."
                }
            ]
        elif is_library:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Small Collection",
                    'Differentiation_Criteria_10': 'Collection Size',
                    'Description_10': f"{desc_8} Small specialized collections and archives."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Medium Collection",
                    'Differentiation_Criteria_10': 'Collection Size',
                    'Description_10': f"{desc_8} Medium-sized collections and libraries."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Large Collection",
                    'Differentiation_Criteria_10': 'Collection Size',
                    'Description_10': f"{desc_8} Large comprehensive collections."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Digital/Online Archive",
                    'Differentiation_Criteria_10': 'Access Model',
                    'Description_10': f"{desc_8} Digital and online archive platforms."
                }
            ]
        else:
            return self.generate_generic(naics_8, title_8, criteria_8, desc_8)

    # ========== SECTOR 52: FINANCE & INSURANCE ==========

    def generate_finance(self, naics_6: str, naics_8: str, title_8: str,
                        criteria_8: str, desc_8: str) -> List[Dict]:
        """Finance and insurance with institution size and service model differentiation"""
        title_lower = title_8.lower()

        is_banking = any(word in title_lower for word in ['bank', 'credit union', 'savings'])
        is_investment = any(word in title_lower for word in ['investment', 'securities', 'broker', 'advisor'])
        is_insurance = 'insurance' in title_lower

        if is_banking:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Community Bank (<$1B assets)",
                    'Differentiation_Criteria_10': 'Institution Size',
                    'Description_10': f"{desc_8} Community banks with under $1 billion in assets."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Regional Bank ($1B-$10B)",
                    'Differentiation_Criteria_10': 'Institution Size',
                    'Description_10': f"{desc_8} Regional banks with $1-10 billion in assets."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Super-Regional Bank ($10B-$100B)",
                    'Differentiation_Criteria_10': 'Institution Size',
                    'Description_10': f"{desc_8} Super-regional banks with $10-100 billion in assets."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - National/Money Center Bank ($100B+)",
                    'Differentiation_Criteria_10': 'Institution Size',
                    'Description_10': f"{desc_8} National and money center banks over $100 billion."
                },
                {
                    'NAICS_10_Digit': naics_8 + '05',
                    'NAICS_10_Title': f"{title_8} - Digital/Neobank",
                    'Differentiation_Criteria_10': 'Business Model',
                    'Description_10': f"{desc_8} Digital-first and neobank operations."
                }
            ]
        elif is_investment:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Independent/RIA Firm",
                    'Differentiation_Criteria_10': 'Firm Type',
                    'Description_10': f"{desc_8} Independent registered investment advisor firms."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Wirehouse/Full-Service",
                    'Differentiation_Criteria_10': 'Firm Type',
                    'Description_10': f"{desc_8} Major wirehouse and full-service brokerage firms."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Discount/Online Broker",
                    'Differentiation_Criteria_10': 'Service Model',
                    'Description_10': f"{desc_8} Discount and online brokerage platforms."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Robo-Advisor/Automated",
                    'Differentiation_Criteria_10': 'Service Model',
                    'Description_10': f"{desc_8} Automated investment and robo-advisor platforms."
                }
            ]
        elif is_insurance:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Independent Agency",
                    'Differentiation_Criteria_10': 'Distribution Model',
                    'Description_10': f"{desc_8} Independent insurance agencies representing multiple carriers."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Captive Agency",
                    'Differentiation_Criteria_10': 'Distribution Model',
                    'Description_10': f"{desc_8} Captive agents representing single insurance carrier."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Direct/Online Insurer",
                    'Differentiation_Criteria_10': 'Distribution Model',
                    'Description_10': f"{desc_8} Direct-to-consumer and online insurance providers."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Reinsurer/Specialty Markets",
                    'Differentiation_Criteria_10': 'Market Type',
                    'Description_10': f"{desc_8} Reinsurance and specialty insurance markets."
                }
            ]
        else:
            return self.generate_generic(naics_8, title_8, criteria_8, desc_8)

    # ========== SECTOR 53: REAL ESTATE & RENTAL ==========

    def generate_realestate(self, naics_6: str, naics_8: str, title_8: str,
                           criteria_8: str, desc_8: str) -> List[Dict]:
        """Real estate with property type and business model differentiation"""
        return [
            {
                'NAICS_10_Digit': naics_8 + '01',
                'NAICS_10_Title': f"{title_8} - Independent/Boutique",
                'Differentiation_Criteria_10': 'Company Size',
                'Description_10': f"{desc_8} Independent and boutique real estate firms."
            },
            {
                'NAICS_10_Digit': naics_8 + '02',
                'NAICS_10_Title': f"{title_8} - Regional Firm",
                'Differentiation_Criteria_10': 'Company Size',
                'Description_10': f"{desc_8} Regional real estate companies with multiple offices."
            },
            {
                'NAICS_10_Digit': naics_8 + '03',
                'NAICS_10_Title': f"{title_8} - National Franchise/Chain",
                'Differentiation_Criteria_10': 'Company Size',
                'Description_10': f"{desc_8} National franchise brands and large firms."
            },
            {
                'NAICS_10_Digit': naics_8 + '04',
                'NAICS_10_Title': f"{title_8} - Luxury/High-End Specialist",
                'Differentiation_Criteria_10': 'Market Segment',
                'Description_10': f"{desc_8} Specialists in luxury and high-end real estate markets."
            },
            {
                'NAICS_10_Digit': naics_8 + '05',
                'NAICS_10_Title': f"{title_8} - PropTech/Digital Platform",
                'Differentiation_Criteria_10': 'Business Model',
                'Description_10': f"{desc_8} Technology-enabled and digital real estate platforms."
            }
        ]

    # ========== SECTOR 54: PROFESSIONAL, SCIENTIFIC & TECHNICAL SERVICES ==========

    def generate_professional(self, naics_6: str, naics_8: str, title_8: str,
                             criteria_8: str, desc_8: str) -> List[Dict]:
        """Professional services with firm size and specialization differentiation"""
        title_lower = title_8.lower()

        is_legal = 'law' in title_lower or 'legal' in title_lower or 'attorney' in title_lower
        is_accounting = any(word in title_lower for word in ['accounting', 'audit', 'tax', 'cpa'])
        is_consulting = 'consult' in title_lower

        if is_legal:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Solo Practitioner",
                    'Differentiation_Criteria_10': 'Firm Size',
                    'Description_10': f"{desc_8} Solo practitioners and single-attorney practices."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Small Firm (2-10 attorneys)",
                    'Differentiation_Criteria_10': 'Firm Size',
                    'Description_10': f"{desc_8} Small law firms with 2-10 attorneys."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Mid-Size Firm (11-100 attorneys)",
                    'Differentiation_Criteria_10': 'Firm Size',
                    'Description_10': f"{desc_8} Mid-sized firms with 11-100 attorneys."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Large/AmLaw Firm (100+ attorneys)",
                    'Differentiation_Criteria_10': 'Firm Size',
                    'Description_10': f"{desc_8} Large law firms and AmLaw-ranked practices."
                },
                {
                    'NAICS_10_Digit': naics_8 + '05',
                    'NAICS_10_Title': f"{title_8} - Virtual/Tech-Enabled Practice",
                    'Differentiation_Criteria_10': 'Service Model',
                    'Description_10': f"{desc_8} Virtual and technology-enabled legal practices."
                }
            ]
        elif is_accounting:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Solo/Small Practice",
                    'Differentiation_Criteria_10': 'Firm Size',
                    'Description_10': f"{desc_8} Solo practitioners and small accounting practices."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Local/Regional Firm",
                    'Differentiation_Criteria_10': 'Firm Size',
                    'Description_10': f"{desc_8} Local and regional accounting firms."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - National Firm",
                    'Differentiation_Criteria_10': 'Firm Size',
                    'Description_10': f"{desc_8} National accounting and consulting firms."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Big 4/International Firm",
                    'Differentiation_Criteria_10': 'Firm Size',
                    'Description_10': f"{desc_8} Big 4 and major international accounting firms."
                }
            ]
        else:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Independent Consultant",
                    'Differentiation_Criteria_10': 'Firm Size',
                    'Description_10': f"{desc_8} Independent consultants and solo practitioners."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Small Firm (<20 employees)",
                    'Differentiation_Criteria_10': 'Firm Size',
                    'Description_10': f"{desc_8} Small professional firms under 20 employees."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Medium Firm (20-100 employees)",
                    'Differentiation_Criteria_10': 'Firm Size',
                    'Description_10': f"{desc_8} Medium firms with 20-100 employees."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Large Firm (100+ employees)",
                    'Differentiation_Criteria_10': 'Firm Size',
                    'Description_10': f"{desc_8} Large professional service firms over 100 employees."
                }
            ]

    # ========== SECTOR 55: MANAGEMENT OF COMPANIES ==========

    def generate_management(self, naics_6: str, naics_8: str, title_8: str,
                           criteria_8: str, desc_8: str) -> List[Dict]:
        """Management of companies differentiation"""
        return [
            {
                'NAICS_10_Digit': naics_8 + '01',
                'NAICS_10_Title': f"{title_8} - Small Holding Company",
                'Differentiation_Criteria_10': 'Company Size',
                'Description_10': f"{desc_8} Small holding companies managing few subsidiaries."
            },
            {
                'NAICS_10_Digit': naics_8 + '02',
                'NAICS_10_Title': f"{title_8} - Regional Holding Company",
                'Differentiation_Criteria_10': 'Company Size',
                'Description_10': f"{desc_8} Regional holding companies with multiple subsidiaries."
            },
            {
                'NAICS_10_Digit': naics_8 + '03',
                'NAICS_10_Title': f"{title_8} - National/Conglomerate",
                'Differentiation_Criteria_10': 'Company Size',
                'Description_10': f"{desc_8} National conglomerates managing diverse businesses."
            },
            {
                'NAICS_10_Digit': naics_8 + '04',
                'NAICS_10_Title': f"{title_8} - Private Equity/Investment Firm",
                'Differentiation_Criteria_10': 'Management Style',
                'Description_10': f"{desc_8} Private equity and investment firms managing portfolio companies."
            }
        ]

    # ========== SECTOR 56: ADMINISTRATIVE & SUPPORT SERVICES ==========

    def generate_administrative(self, naics_6: str, naics_8: str, title_8: str,
                               criteria_8: str, desc_8: str) -> List[Dict]:
        """Administrative services with service scope differentiation"""
        return [
            {
                'NAICS_10_Digit': naics_8 + '01',
                'NAICS_10_Title': f"{title_8} - Local/Small Operation",
                'Differentiation_Criteria_10': 'Service Scope',
                'Description_10': f"{desc_8} Local small-scale service providers."
            },
            {
                'NAICS_10_Digit': naics_8 + '02',
                'NAICS_10_Title': f"{title_8} - Regional Provider",
                'Differentiation_Criteria_10': 'Service Scope',
                'Description_10': f"{desc_8} Regional service providers covering multiple markets."
            },
            {
                'NAICS_10_Digit': naics_8 + '03',
                'NAICS_10_Title': f"{title_8} - National Service Company",
                'Differentiation_Criteria_10': 'Service Scope',
                'Description_10': f"{desc_8} National companies with multi-state coverage."
            },
            {
                'NAICS_10_Digit': naics_8 + '04',
                'NAICS_10_Title': f"{title_8} - Specialized/Niche Provider",
                'Differentiation_Criteria_10': 'Service Focus',
                'Description_10': f"{desc_8} Providers specializing in specific industries or services."
            }
        ]

    # ========== SECTOR 61: EDUCATIONAL SERVICES ==========

    def generate_education(self, naics_6: str, naics_8: str, title_8: str,
                          criteria_8: str, desc_8: str) -> List[Dict]:
        """Educational services with institution type and delivery model differentiation"""
        title_lower = title_8.lower()

        is_higher_ed = any(word in title_lower for word in ['college', 'university', 'higher education'])
        is_k12 = any(word in title_lower for word in ['school', 'elementary', 'secondary', 'k-12'])

        if is_higher_ed:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Small Private (<1,000 students)",
                    'Differentiation_Criteria_10': 'Institution Size',
                    'Description_10': f"{desc_8} Small private institutions under 1,000 students."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Medium (1,000-5,000 students)",
                    'Differentiation_Criteria_10': 'Institution Size',
                    'Description_10': f"{desc_8} Medium institutions with 1,000-5,000 students."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Large (5,000+ students)",
                    'Differentiation_Criteria_10': 'Institution Size',
                    'Description_10': f"{desc_8} Large institutions with over 5,000 students."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Online/Distance Learning",
                    'Differentiation_Criteria_10': 'Delivery Model',
                    'Description_10': f"{desc_8} Primarily online and distance learning institutions."
                }
            ]
        else:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Single Location",
                    'Differentiation_Criteria_10': 'Organization Size',
                    'Description_10': f"{desc_8} Single location educational services."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Small Chain (2-5 locations)",
                    'Differentiation_Criteria_10': 'Organization Size',
                    'Description_10': f"{desc_8} Small chains with 2-5 locations."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Regional/National Chain",
                    'Differentiation_Criteria_10': 'Organization Size',
                    'Description_10': f"{desc_8} Regional or national educational chains."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Franchise Operation",
                    'Differentiation_Criteria_10': 'Business Model',
                    'Description_10': f"{desc_8} Franchise-based educational services."
                }
            ]

    # ========== SECTOR 62: HEALTH CARE & SOCIAL ASSISTANCE ==========

    def generate_healthcare(self, naics_6: str, naics_8: str, title_8: str,
                           criteria_8: str, desc_8: str) -> List[Dict]:
        """Healthcare with facility size and care model differentiation"""
        title_lower = title_8.lower()

        # Hospitals and inpatient facilities
        is_hospital = 'hospital' in title_lower

        # Physician and medical offices
        is_physician = any(word in title_lower for word in [
            'physician', 'doctor', 'medical practice', 'cardiologist', 'dermatologist',
            'gastroenterologist', 'oncologist', 'orthopedic', 'ob/gyn', 'obgyn',
            'ophthalmologist', 'ent specialist', 'urologist', 'neurologist',
            'pulmonologist', 'endocrinologist', 'family medicine', 'internal medicine',
            'pediatrician', 'surgeon'
        ])

        # Dental practices
        is_dental = any(word in title_lower for word in [
            'dent', 'orthodont', 'periodon', 'endodont', 'oral surgery', 'prosthodon'
        ])

        # Mental health services
        is_mental_health = any(word in title_lower for word in [
            'psychiatrist', 'psychologist', 'therapist', 'counselor', 'counseling',
            'mental health', 'behavioral health', 'substance abuse', 'addiction'
        ])

        # Diagnostic and testing services
        is_diagnostic = any(word in title_lower for word in [
            'lab', 'laboratory', 'diagnostic', 'imaging', 'radiology', 'ct scan',
            'mri', 'ultrasound', 'x-ray', 'blood bank', 'pathology'
        ])

        # Outpatient care centers
        is_outpatient = any(word in title_lower for word in [
            'outpatient', 'ambulatory', 'surgery center', 'urgent care', 'walk-in clinic',
            'treatment center', 'dialysis'
        ])

        # Nursing and home health
        is_nursing = any(word in title_lower for word in [
            'nursing', 'home health', 'hospice', 'visiting nurse', 'home care'
        ])

        # Long-term care and assisted living
        is_long_term_care = any(word in title_lower for word in [
            'assisted living', 'nursing home', 'skilled nursing', 'long-term care',
            'nursing facility', 'residential care', 'board and care', 'memory care'
        ])

        # Allied health practitioners
        is_allied_health = any(word in title_lower for word in [
            'chiropract', 'optometr', 'podiatr', 'physical therap', 'occupational therap',
            'speech therap', 'audiolog', 'acupuncture'
        ])

        # Day care and child care
        is_daycare = any(word in title_lower for word in [
            'day care', 'daycare', 'child care', 'childcare', 'preschool', 'after-school'
        ])

        # Social services
        is_social_services = any(word in title_lower for word in [
            'adoption', 'foster', 'intervention', 'relief', 'advocacy', 'crisis'
        ])

        if is_hospital:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Small Hospital (<100 beds)",
                    'Differentiation_Criteria_10': 'Facility Size',
                    'Description_10': f"{desc_8} Small hospitals under 100 beds, typically rural."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Medium Hospital (100-400 beds)",
                    'Differentiation_Criteria_10': 'Facility Size',
                    'Description_10': f"{desc_8} Medium community hospitals with 100-400 beds."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Large Hospital (400+ beds)",
                    'Differentiation_Criteria_10': 'Facility Size',
                    'Description_10': f"{desc_8} Large regional or academic medical centers over 400 beds."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Health System Facility",
                    'Differentiation_Criteria_10': 'Ownership Model',
                    'Description_10': f"{desc_8} Hospitals part of integrated delivery networks."
                }
            ]
        elif is_physician:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Solo Practice",
                    'Differentiation_Criteria_10': 'Practice Size',
                    'Description_10': f"{desc_8} Single physician solo practices."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Small Group (2-5 physicians)",
                    'Differentiation_Criteria_10': 'Practice Size',
                    'Description_10': f"{desc_8} Small physician groups with 2-5 doctors."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Medium Group (6-20 physicians)",
                    'Differentiation_Criteria_10': 'Practice Size',
                    'Description_10': f"{desc_8} Medium groups with 6-20 physicians."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Large Group (20+ physicians)",
                    'Differentiation_Criteria_10': 'Practice Size',
                    'Description_10': f"{desc_8} Large physician groups and medical groups over 20 doctors."
                },
                {
                    'NAICS_10_Digit': naics_8 + '05',
                    'NAICS_10_Title': f"{title_8} - Hospital-Employed",
                    'Differentiation_Criteria_10': 'Employment Model',
                    'Description_10': f"{desc_8} Hospital-employed physician practices."
                }
            ]
        elif is_dental:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Solo Practitioner",
                    'Differentiation_Criteria_10': 'Practice Size',
                    'Description_10': f"{desc_8} Single dentist solo practices."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Small Group (2-5 dentists)",
                    'Differentiation_Criteria_10': 'Practice Size',
                    'Description_10': f"{desc_8} Small dental groups with 2-5 dentists."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Large Group/DSO (6+ dentists)",
                    'Differentiation_Criteria_10': 'Practice Size',
                    'Description_10': f"{desc_8} Large groups and dental service organizations with 6+ dentists."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Corporate Chain",
                    'Differentiation_Criteria_10': 'Business Model',
                    'Description_10': f"{desc_8} Corporate dental chains with multiple locations."
                }
            ]
        elif is_mental_health:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Solo Private Practice",
                    'Differentiation_Criteria_10': 'Practice Size',
                    'Description_10': f"{desc_8} Independent solo practitioners."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Small Group Practice",
                    'Differentiation_Criteria_10': 'Practice Size',
                    'Description_10': f"{desc_8} Small group practices with multiple providers."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Outpatient Clinic/Center",
                    'Differentiation_Criteria_10': 'Facility Type',
                    'Description_10': f"{desc_8} Outpatient mental health clinics and counseling centers."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Inpatient Treatment Facility",
                    'Differentiation_Criteria_10': 'Facility Type',
                    'Description_10': f"{desc_8} Inpatient psychiatric or substance abuse treatment facilities."
                },
                {
                    'NAICS_10_Digit': naics_8 + '05',
                    'NAICS_10_Title': f"{title_8} - Community Mental Health Center",
                    'Differentiation_Criteria_10': 'Service Model',
                    'Description_10': f"{desc_8} Community-based comprehensive mental health centers."
                }
            ]
        elif is_diagnostic:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Independent Facility",
                    'Differentiation_Criteria_10': 'Ownership Model',
                    'Description_10': f"{desc_8} Independent diagnostic and testing facilities."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Hospital-Based Service",
                    'Differentiation_Criteria_10': 'Ownership Model',
                    'Description_10': f"{desc_8} Hospital-based or hospital-affiliated services."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Regional Chain",
                    'Differentiation_Criteria_10': 'Organization Size',
                    'Description_10': f"{desc_8} Regional chains with multiple locations."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - National Laboratory Network",
                    'Differentiation_Criteria_10': 'Organization Size',
                    'Description_10': f"{desc_8} National laboratory networks and reference labs."
                }
            ]
        elif is_outpatient:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Single-Specialty Center",
                    'Differentiation_Criteria_10': 'Service Scope',
                    'Description_10': f"{desc_8} Single-specialty outpatient centers."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Multi-Specialty Center",
                    'Differentiation_Criteria_10': 'Service Scope',
                    'Description_10': f"{desc_8} Multi-specialty outpatient care centers."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Hospital-Affiliated",
                    'Differentiation_Criteria_10': 'Ownership Model',
                    'Description_10': f"{desc_8} Hospital-owned or affiliated outpatient centers."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Physician-Owned",
                    'Differentiation_Criteria_10': 'Ownership Model',
                    'Description_10': f"{desc_8} Physician-owned outpatient facilities."
                }
            ]
        elif is_nursing:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Small Agency (<20 staff)",
                    'Differentiation_Criteria_10': 'Agency Size',
                    'Description_10': f"{desc_8} Small home health agencies under 20 staff."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Medium Agency (20-100 staff)",
                    'Differentiation_Criteria_10': 'Agency Size',
                    'Description_10': f"{desc_8} Medium agencies with 20-100 staff members."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Large Agency (100+ staff)",
                    'Differentiation_Criteria_10': 'Agency Size',
                    'Description_10': f"{desc_8} Large home health organizations over 100 staff."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - National Chain/Network",
                    'Differentiation_Criteria_10': 'Organization Type',
                    'Description_10': f"{desc_8} National chains and integrated networks."
                }
            ]
        elif is_long_term_care:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Small Facility (<50 beds)",
                    'Differentiation_Criteria_10': 'Facility Size',
                    'Description_10': f"{desc_8} Small facilities under 50 beds or units."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Medium Facility (50-150 beds)",
                    'Differentiation_Criteria_10': 'Facility Size',
                    'Description_10': f"{desc_8} Medium facilities with 50-150 beds or units."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Large Facility (150+ beds)",
                    'Differentiation_Criteria_10': 'Facility Size',
                    'Description_10': f"{desc_8} Large facilities over 150 beds or units."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Multi-Facility Organization",
                    'Differentiation_Criteria_10': 'Organization Type',
                    'Description_10': f"{desc_8} Organizations operating multiple facilities."
                }
            ]
        elif is_allied_health:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Solo Practitioner",
                    'Differentiation_Criteria_10': 'Practice Size',
                    'Description_10': f"{desc_8} Solo practitioners and single-location practices."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Small Group Practice",
                    'Differentiation_Criteria_10': 'Practice Size',
                    'Description_10': f"{desc_8} Small group practices with multiple providers."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Multi-Location Practice",
                    'Differentiation_Criteria_10': 'Practice Size',
                    'Description_10': f"{desc_8} Practices with multiple locations."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Corporate Chain/Franchise",
                    'Differentiation_Criteria_10': 'Business Model',
                    'Description_10': f"{desc_8} Corporate chains and franchise operations."
                }
            ]
        elif is_daycare or is_social_services:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Single Location",
                    'Differentiation_Criteria_10': 'Operation Size',
                    'Description_10': f"{desc_8} Single location operations."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Small Multi-Site (2-5 locations)",
                    'Differentiation_Criteria_10': 'Operation Size',
                    'Description_10': f"{desc_8} Small organizations with 2-5 locations."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Regional Organization",
                    'Differentiation_Criteria_10': 'Operation Size',
                    'Description_10': f"{desc_8} Regional organizations serving multiple communities."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - National/Chain Operation",
                    'Differentiation_Criteria_10': 'Operation Size',
                    'Description_10': f"{desc_8} National chains or large-scale operations."
                }
            ]
        else:
            return self.generate_generic(naics_8, title_8, criteria_8, desc_8)

    # ========== SECTOR 71: ARTS, ENTERTAINMENT & RECREATION ==========

    def generate_arts(self, naics_6: str, naics_8: str, title_8: str,
                     criteria_8: str, desc_8: str) -> List[Dict]:
        """Arts and entertainment with venue size and business model differentiation"""
        return [
            {
                'NAICS_10_Digit': naics_8 + '01',
                'NAICS_10_Title': f"{title_8} - Independent/Small Venue",
                'Differentiation_Criteria_10': 'Operation Size',
                'Description_10': f"{desc_8} Independent operators and small venues."
            },
            {
                'NAICS_10_Digit': naics_8 + '02',
                'NAICS_10_Title': f"{title_8} - Regional Operation",
                'Differentiation_Criteria_10': 'Operation Size',
                'Description_10': f"{desc_8} Regional operators with multiple locations."
            },
            {
                'NAICS_10_Digit': naics_8 + '03',
                'NAICS_10_Title': f"{title_8} - National/Chain Operation",
                'Differentiation_Criteria_10': 'Operation Size',
                'Description_10': f"{desc_8} National chains and large entertainment companies."
            },
            {
                'NAICS_10_Digit': naics_8 + '04',
                'NAICS_10_Title': f"{title_8} - Premium/Luxury Experience",
                'Differentiation_Criteria_10': 'Market Positioning',
                'Description_10': f"{desc_8} Premium and luxury entertainment experiences."
            }
        ]

    # ========== SECTOR 72: ACCOMMODATION & FOOD SERVICES ==========

    def generate_accommodation(self, naics_6: str, naics_8: str, title_8: str,
                               criteria_8: str, desc_8: str) -> List[Dict]:
        """Accommodation and food services with establishment type differentiation"""
        title_lower = title_8.lower()

        is_lodging = any(word in title_lower for word in [
            'hotel', 'motel', 'lodging', 'accommodation', 'casino hotel', 'resort',
            'inn', 'bed-and-breakfast', 'b&b'
        ])

        is_alt_lodging = any(word in title_lower for word in [
            'rv park', 'campground', 'camping', 'rooming house', 'boarding house'
        ])

        is_restaurant = any(word in title_lower for word in [
            'restaurant', 'dining', 'full-service', 'limited-service', 'fast food',
            'quick service', 'fine dining', 'casual dining'
        ])

        is_cafeteria = any(word in title_lower for word in ['cafeteria', 'buffet', 'grill buffet'])

        is_caterer = any(word in title_lower for word in ['caterer', 'catering', 'food contractor'])

        is_mobile_food = any(word in title_lower for word in ['mobile food', 'food truck', 'street vendor'])

        is_bar = any(word in title_lower for word in ['drinking place', 'bar', 'tavern', 'pub', 'nightclub'])

        is_snack = any(word in title_lower for word in ['snack bar', 'juice bar', 'coffee shop', 'cafe'])

        if is_lodging:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Independent Property",
                    'Differentiation_Criteria_10': 'Ownership Model',
                    'Description_10': f"{desc_8} Independent lodging properties."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Franchise Property",
                    'Differentiation_Criteria_10': 'Ownership Model',
                    'Description_10': f"{desc_8} Franchise-branded lodging properties."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Chain-Managed Property",
                    'Differentiation_Criteria_10': 'Ownership Model',
                    'Description_10': f"{desc_8} Corporate chain-managed properties."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Boutique/Luxury",
                    'Differentiation_Criteria_10': 'Market Segment',
                    'Description_10': f"{desc_8} Boutique and luxury hospitality properties."
                }
            ]
        elif is_restaurant:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Independent Single Unit",
                    'Differentiation_Criteria_10': 'Operation Type',
                    'Description_10': f"{desc_8} Independent single-location restaurants."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Small Chain (2-10 units)",
                    'Differentiation_Criteria_10': 'Operation Type',
                    'Description_10': f"{desc_8} Small restaurant groups with 2-10 locations."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Regional Chain (11-100 units)",
                    'Differentiation_Criteria_10': 'Operation Type',
                    'Description_10': f"{desc_8} Regional chains with 11-100 locations."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - National Chain (100+ units)",
                    'Differentiation_Criteria_10': 'Operation Type',
                    'Description_10': f"{desc_8} National restaurant chains with over 100 locations."
                },
                {
                    'NAICS_10_Digit': naics_8 + '05',
                    'NAICS_10_Title': f"{title_8} - Franchise Operation",
                    'Differentiation_Criteria_10': 'Operation Type',
                    'Description_10': f"{desc_8} Franchise-operated restaurant locations."
                }
            ]
        elif is_alt_lodging:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Small Operation (1-20 sites/rooms)",
                    'Differentiation_Criteria_10': 'Operation Size',
                    'Description_10': f"{desc_8} Small operations with 1-20 sites or rooms."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Medium Operation (21-100 sites/rooms)",
                    'Differentiation_Criteria_10': 'Operation Size',
                    'Description_10': f"{desc_8} Medium operations with 21-100 sites or rooms."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Large Operation (100+ sites/rooms)",
                    'Differentiation_Criteria_10': 'Operation Size',
                    'Description_10': f"{desc_8} Large operations with over 100 sites or rooms."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Budget/Economy",
                    'Differentiation_Criteria_10': 'Market Segment',
                    'Description_10': f"{desc_8} Budget and economy lodging options."
                }
            ]
        elif is_cafeteria:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Corporate/Office",
                    'Differentiation_Criteria_10': 'Service Setting',
                    'Description_10': f"{desc_8} Corporate and office building cafeterias."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Healthcare Facility",
                    'Differentiation_Criteria_10': 'Service Setting',
                    'Description_10': f"{desc_8} Hospital and healthcare facility cafeterias."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Educational Institution",
                    'Differentiation_Criteria_10': 'Service Setting',
                    'Description_10': f"{desc_8} School, college, and university cafeterias."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Stand-Alone Buffet",
                    'Differentiation_Criteria_10': 'Service Model',
                    'Description_10': f"{desc_8} Stand-alone buffet restaurants."
                }
            ]
        elif is_caterer:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Small Caterer (<50 events/year)",
                    'Differentiation_Criteria_10': 'Business Size',
                    'Description_10': f"{desc_8} Small catering operations under 50 events annually."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Medium Caterer (50-200 events/year)",
                    'Differentiation_Criteria_10': 'Business Size',
                    'Description_10': f"{desc_8} Medium catering companies 50-200 events annually."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Large Caterer (200+ events/year)",
                    'Differentiation_Criteria_10': 'Business Size',
                    'Description_10': f"{desc_8} Large catering operations over 200 events annually."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Corporate Food Services",
                    'Differentiation_Criteria_10': 'Service Type',
                    'Description_10': f"{desc_8} Corporate and institutional food service contractors."
                }
            ]
        elif is_mobile_food:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Single Unit Owner-Operator",
                    'Differentiation_Criteria_10': 'Operation Size',
                    'Description_10': f"{desc_8} Single vehicle owner-operator."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Small Fleet (2-5 units)",
                    'Differentiation_Criteria_10': 'Operation Size',
                    'Description_10': f"{desc_8} Small fleet with 2-5 mobile units."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Large Fleet (6+ units)",
                    'Differentiation_Criteria_10': 'Operation Size',
                    'Description_10': f"{desc_8} Large fleet with 6 or more mobile units."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Gourmet/Specialty Food Truck",
                    'Differentiation_Criteria_10': 'Market Positioning',
                    'Description_10': f"{desc_8} Gourmet and specialty food truck operations."
                }
            ]
        elif is_bar:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Neighborhood Bar/Pub",
                    'Differentiation_Criteria_10': 'Establishment Type',
                    'Description_10': f"{desc_8} Neighborhood bars and local pubs."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Sports Bar",
                    'Differentiation_Criteria_10': 'Establishment Type',
                    'Description_10': f"{desc_8} Sports bars and sports-themed establishments."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Nightclub/Dance Club",
                    'Differentiation_Criteria_10': 'Establishment Type',
                    'Description_10': f"{desc_8} Nightclubs and dance clubs."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Upscale Cocktail Bar",
                    'Differentiation_Criteria_10': 'Market Segment',
                    'Description_10': f"{desc_8} Upscale cocktail bars and lounges."
                }
            ]
        elif is_snack:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Independent Single Location",
                    'Differentiation_Criteria_10': 'Business Model',
                    'Description_10': f"{desc_8} Independent single-location operations."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Small Chain (2-10 units)",
                    'Differentiation_Criteria_10': 'Business Model',
                    'Description_10': f"{desc_8} Small chains with 2-10 locations."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Regional/National Chain",
                    'Differentiation_Criteria_10': 'Business Model',
                    'Description_10': f"{desc_8} Regional and national chain operations."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Specialty/Gourmet",
                    'Differentiation_Criteria_10': 'Market Positioning',
                    'Description_10': f"{desc_8} Specialty and gourmet snack bars."
                }
            ]
        else:
            return self.generate_generic(naics_8, title_8, criteria_8, desc_8)

    # ========== SECTOR 81: OTHER SERVICES ==========

    def generate_other_services(self, naics_6: str, naics_8: str, title_8: str,
                               criteria_8: str, desc_8: str) -> List[Dict]:
        """Other services with industry-specific differentiation"""
        title_lower = title_8.lower()

        # Automotive repair services
        is_auto_repair = any(word in title_lower for word in [
            'auto repair', 'automotive repair', 'car repair', 'vehicle repair',
            'oil change', 'transmission', 'muffler', 'exhaust', 'brake', 'tire',
            'body shop', 'collision', 'paint', 'auto glass', 'auto electric'
        ])

        # Car wash services
        is_car_wash = any(word in title_lower for word in ['car wash', 'auto detailing', 'detailing'])

        # Electronic repair
        is_electronic_repair = any(word in title_lower for word in [
            'computer repair', 'laptop repair', 'smartphone', 'tablet repair',
            'electronics repair', 'phone repair', 'tv repair', 'game console'
        ])

        # Commercial/industrial machinery repair
        is_machinery_repair = any(word in title_lower for word in [
            'hvac', 'refrigeration', 'commercial equipment', 'industrial equipment',
            'restaurant equipment', 'forklift', 'material handling', 'pump', 'compressor'
        ])

        # Appliance and household repair
        is_appliance_repair = any(word in title_lower for word in [
            'appliance repair', 'refrigerator repair', 'washer', 'dryer',
            'furniture repair', 'upholstery', 'footwear repair', 'shoe repair'
        ])

        # Personal care services
        is_personal_care = any(word in title_lower for word in [
            'barber', 'beauty salon', 'hair salon', 'nail salon', 'spa',
            'esthetician', 'cosmetology', 'manicure', 'pedicure', 'grooming',
            'hair cutting', 'styling'
        ])

        # Funeral services
        is_funeral = any(word in title_lower for word in ['funeral', 'crematory', 'cemetery', 'mortuary'])

        # Laundry and drycleaning
        is_laundry = any(word in title_lower for word in [
            'laundry', 'drycleaning', 'dry cleaning', 'linen supply', 'laundromat', 'coin-operated'
        ])

        # Pet care services
        is_pet_care = any(word in title_lower for word in [
            'pet care', 'pet grooming', 'pet boarding', 'kennel', 'pet day care', 'dog grooming'
        ])

        # Parking services
        is_parking = any(word in title_lower for word in ['parking', 'garage', 'valet'])

        # Organizations (religious, civic, professional, etc.)
        is_organization = any(word in title_lower for word in [
            'religious organization', 'church', 'civic organization', 'professional organization',
            'business association', 'labor union', 'foundation', 'grantmaking',
            'social advocacy', 'nonprofit', 'charitable organization', 'volunteer'
        ])

        if is_auto_repair:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Independent Shop (1-2 bays)",
                    'Differentiation_Criteria_10': 'Shop Size',
                    'Description_10': f"{desc_8} Small independent shops with 1-2 service bays."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Mid-Size Shop (3-8 bays)",
                    'Differentiation_Criteria_10': 'Shop Size',
                    'Description_10': f"{desc_8} Mid-size repair facilities with 3-8 bays."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Large Shop (9+ bays)",
                    'Differentiation_Criteria_10': 'Shop Size',
                    'Description_10': f"{desc_8} Large repair centers with 9 or more service bays."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - National Chain/Franchise",
                    'Differentiation_Criteria_10': 'Business Model',
                    'Description_10': f"{desc_8} National chain and franchise operations."
                },
                {
                    'NAICS_10_Digit': naics_8 + '05',
                    'NAICS_10_Title': f"{title_8} - Mobile Service",
                    'Differentiation_Criteria_10': 'Service Model',
                    'Description_10': f"{desc_8} Mobile repair services operating on-location."
                }
            ]
        elif is_car_wash:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Single Location",
                    'Differentiation_Criteria_10': 'Operation Size',
                    'Description_10': f"{desc_8} Single-location car wash operations."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Regional Chain (2-10 locations)",
                    'Differentiation_Criteria_10': 'Operation Size',
                    'Description_10': f"{desc_8} Regional chains with 2-10 locations."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Large Chain (11+ locations)",
                    'Differentiation_Criteria_10': 'Operation Size',
                    'Description_10': f"{desc_8} Large multi-location chains."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Express/Automated",
                    'Differentiation_Criteria_10': 'Service Model',
                    'Description_10': f"{desc_8} High-volume automated express operations."
                }
            ]
        elif is_electronic_repair:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Independent Repair Shop",
                    'Differentiation_Criteria_10': 'Business Model',
                    'Description_10': f"{desc_8} Independent local repair shops."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Chain/Franchise Operation",
                    'Differentiation_Criteria_10': 'Business Model',
                    'Description_10': f"{desc_8} National chain and franchise repair centers."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Manufacturer Authorized Service",
                    'Differentiation_Criteria_10': 'Authorization Level',
                    'Description_10': f"{desc_8} Manufacturer authorized and certified repair centers."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Mail-In/Online Service",
                    'Differentiation_Criteria_10': 'Service Model',
                    'Description_10': f"{desc_8} Mail-in and online repair services."
                }
            ]
        elif is_machinery_repair:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Small Service Company (1-5 techs)",
                    'Differentiation_Criteria_10': 'Company Size',
                    'Description_10': f"{desc_8} Small service companies with 1-5 technicians."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Regional Service Provider (6-20 techs)",
                    'Differentiation_Criteria_10': 'Company Size',
                    'Description_10': f"{desc_8} Regional providers with 6-20 technicians."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Large Service Company (21+ techs)",
                    'Differentiation_Criteria_10': 'Company Size',
                    'Description_10': f"{desc_8} Large service companies with 21+ technicians."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Manufacturer Service Division",
                    'Differentiation_Criteria_10': 'Business Model',
                    'Description_10': f"{desc_8} Factory-owned service and support divisions."
                }
            ]
        elif is_appliance_repair:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Independent Technician",
                    'Differentiation_Criteria_10': 'Business Size',
                    'Description_10': f"{desc_8} Independent owner-operator technicians."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Small Service Company",
                    'Differentiation_Criteria_10': 'Business Size',
                    'Description_10': f"{desc_8} Small service companies with multiple technicians."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Regional Service Network",
                    'Differentiation_Criteria_10': 'Business Size',
                    'Description_10': f"{desc_8} Regional multi-location service networks."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Factory Authorized Service",
                    'Differentiation_Criteria_10': 'Authorization Level',
                    'Description_10': f"{desc_8} Factory authorized and warranty service providers."
                }
            ]
        elif is_personal_care:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Solo Practitioner/Booth Renter",
                    'Differentiation_Criteria_10': 'Business Size',
                    'Description_10': f"{desc_8} Solo practitioners and booth rental arrangements."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Small Salon (2-5 stations)",
                    'Differentiation_Criteria_10': 'Business Size',
                    'Description_10': f"{desc_8} Small salons with 2-5 service stations."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Large Salon (6+ stations)",
                    'Differentiation_Criteria_10': 'Business Size',
                    'Description_10': f"{desc_8} Large salons with 6 or more stations."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Chain/Franchise Operation",
                    'Differentiation_Criteria_10': 'Business Model',
                    'Description_10': f"{desc_8} National chain and franchise salon operations."
                },
                {
                    'NAICS_10_Digit': naics_8 + '05',
                    'NAICS_10_Title': f"{title_8} - Luxury/High-End Establishment",
                    'Differentiation_Criteria_10': 'Market Segment',
                    'Description_10': f"{desc_8} Luxury and high-end service establishments."
                }
            ]
        elif is_funeral:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Independent Family-Owned",
                    'Differentiation_Criteria_10': 'Ownership Model',
                    'Description_10': f"{desc_8} Independent family-owned operations."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Small Chain (2-5 locations)",
                    'Differentiation_Criteria_10': 'Company Size',
                    'Description_10': f"{desc_8} Small regional chains with 2-5 locations."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Large Chain (6+ locations)",
                    'Differentiation_Criteria_10': 'Company Size',
                    'Description_10': f"{desc_8} Large multi-location funeral home chains."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Corporate-Owned/Consolidator",
                    'Differentiation_Criteria_10': 'Ownership Model',
                    'Description_10': f"{desc_8} Corporate consolidators and large operators."
                }
            ]
        elif is_laundry:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Single Location",
                    'Differentiation_Criteria_10': 'Operation Size',
                    'Description_10': f"{desc_8} Single-location operations."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Multi-Location (2-5 stores)",
                    'Differentiation_Criteria_10': 'Operation Size',
                    'Description_10': f"{desc_8} Small chains with 2-5 locations."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Large Chain (6+ stores)",
                    'Differentiation_Criteria_10': 'Operation Size',
                    'Description_10': f"{desc_8} Large chains with 6 or more stores."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Industrial/Commercial Facility",
                    'Differentiation_Criteria_10': 'Service Type',
                    'Description_10': f"{desc_8} Large industrial and commercial laundry facilities."
                }
            ]
        elif is_pet_care:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Independent/Owner-Operated",
                    'Differentiation_Criteria_10': 'Business Size',
                    'Description_10': f"{desc_8} Independent owner-operated pet care services."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Small Facility (2-10 employees)",
                    'Differentiation_Criteria_10': 'Business Size',
                    'Description_10': f"{desc_8} Small facilities with 2-10 employees."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Large Facility (11+ employees)",
                    'Differentiation_Criteria_10': 'Business Size',
                    'Description_10': f"{desc_8} Large facilities with 11 or more employees."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Chain/Franchise",
                    'Differentiation_Criteria_10': 'Business Model',
                    'Description_10': f"{desc_8} National chain and franchise operations."
                }
            ]
        elif is_parking:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Single Facility",
                    'Differentiation_Criteria_10': 'Operation Size',
                    'Description_10': f"{desc_8} Single parking facility operations."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Multi-Facility Operator",
                    'Differentiation_Criteria_10': 'Operation Size',
                    'Description_10': f"{desc_8} Operators managing multiple parking facilities."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - National Parking Company",
                    'Differentiation_Criteria_10': 'Operation Size',
                    'Description_10': f"{desc_8} National parking management companies."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Technology Platform/App-Based",
                    'Differentiation_Criteria_10': 'Business Model',
                    'Description_10': f"{desc_8} Technology platforms and app-based parking services."
                }
            ]
        elif is_organization:
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Local Chapter",
                    'Differentiation_Criteria_10': 'Organization Scope',
                    'Description_10': f"{desc_8} Local chapters and community organizations."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - State/Regional Organization",
                    'Differentiation_Criteria_10': 'Organization Scope',
                    'Description_10': f"{desc_8} State and regional level organizations."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - National Organization",
                    'Differentiation_Criteria_10': 'Organization Scope',
                    'Description_10': f"{desc_8} National-level organizations and associations."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - International Organization",
                    'Differentiation_Criteria_10': 'Organization Scope',
                    'Description_10': f"{desc_8} International and global organizations."
                }
            ]
        else:
            # Generic fallback for other service types
            return [
                {
                    'NAICS_10_Digit': naics_8 + '01',
                    'NAICS_10_Title': f"{title_8} - Independent/Owner-Operated",
                    'Differentiation_Criteria_10': 'Business Size',
                    'Description_10': f"{desc_8} Independent and owner-operated service providers."
                },
                {
                    'NAICS_10_Digit': naics_8 + '02',
                    'NAICS_10_Title': f"{title_8} - Small Business (2-10 employees)",
                    'Differentiation_Criteria_10': 'Business Size',
                    'Description_10': f"{desc_8} Small service businesses with 2-10 employees."
                },
                {
                    'NAICS_10_Digit': naics_8 + '03',
                    'NAICS_10_Title': f"{title_8} - Medium Business (11-50 employees)",
                    'Differentiation_Criteria_10': 'Business Size',
                    'Description_10': f"{desc_8} Medium-sized service operations with 11-50 employees."
                },
                {
                    'NAICS_10_Digit': naics_8 + '04',
                    'NAICS_10_Title': f"{title_8} - Multi-Location/Chain",
                    'Differentiation_Criteria_10': 'Business Model',
                    'Description_10': f"{desc_8} Multi-location service providers and chains."
                }
            ]

    # ========== SECTOR 92: PUBLIC ADMINISTRATION ==========

    def generate_public_admin(self, naics_6: str, naics_8: str, title_8: str,
                             criteria_8: str, desc_8: str) -> List[Dict]:
        """Public administration with jurisdiction level differentiation"""
        return [
            {
                'NAICS_10_Digit': naics_8 + '01',
                'NAICS_10_Title': f"{title_8} - Local/Municipal",
                'Differentiation_Criteria_10': 'Jurisdiction Level',
                'Description_10': f"{desc_8} Local and municipal government operations."
            },
            {
                'NAICS_10_Digit': naics_8 + '02',
                'NAICS_10_Title': f"{title_8} - County/Regional",
                'Differentiation_Criteria_10': 'Jurisdiction Level',
                'Description_10': f"{desc_8} County and regional government operations."
            },
            {
                'NAICS_10_Digit': naics_8 + '03',
                'NAICS_10_Title': f"{title_8} - State/Provincial",
                'Differentiation_Criteria_10': 'Jurisdiction Level',
                'Description_10': f"{desc_8} State and provincial government operations."
            },
            {
                'NAICS_10_Digit': naics_8 + '04',
                'NAICS_10_Title': f"{title_8} - Federal/National",
                'Differentiation_Criteria_10': 'Jurisdiction Level',
                'Description_10': f"{desc_8} Federal and national government operations."
            }
        ]

    def generate_generic(self, naics_8: str, title_8: str,
                        criteria_8: str, desc_8: str) -> List[Dict]:
        """Generic fallback for codes without specific logic"""
        return [
            {
                'NAICS_10_Digit': naics_8 + '01',
                'NAICS_10_Title': f"{title_8} - Small Scale",
                'Differentiation_Criteria_10': 'Business Size',
                'Description_10': f"{desc_8} Small-scale operations."
            },
            {
                'NAICS_10_Digit': naics_8 + '02',
                'NAICS_10_Title': f"{title_8} - Medium Scale",
                'Differentiation_Criteria_10': 'Business Size',
                'Description_10': f"{desc_8} Medium-sized operations."
            },
            {
                'NAICS_10_Digit': naics_8 + '03',
                'NAICS_10_Title': f"{title_8} - Large Scale",
                'Differentiation_Criteria_10': 'Business Size',
                'Description_10': f"{desc_8} Large-scale commercial operations."
            },
            {
                'NAICS_10_Digit': naics_8 + '04',
                'NAICS_10_Title': f"{title_8} - Technology-Enhanced",
                'Differentiation_Criteria_10': 'Technology Level',
                'Description_10': f"{desc_8} Operations with advanced technology integration."
            }
        ]

    def process_file(self) -> str:
        """Process the 8-digit file and generate 10-digit codes"""
        print("Starting 10-digit NAICS code generation...")
        print(f"Reading from: {self.input_file}")

        with open(self.input_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)

            for i, row in enumerate(reader, 1):
                if i % 100 == 0:
                    print(f"  Processed {i} codes...")

                # Generate 10-digit extensions
                extensions = self.generate_extensions(row)

                # Add to output
                for ext in extensions:
                    output_row = {
                        'NAICS_6_Digit': row['NAICS_6_Digit'],
                        'NAICS_6_Title': row['NAICS_6_Title'],
                        'NAICS_8_Digit': row['NAICS_8_Digit'],
                        'NAICS_8_Title': row['NAICS_8_Title'],
                        'Differentiation_Criteria_8': row['Differentiation_Criteria'],
                        'Description_8': row['Description'],
                        'NAICS_10_Digit': ext['NAICS_10_Digit'],
                        'NAICS_10_Title': ext['NAICS_10_Title'],
                        'Differentiation_Criteria_10': ext['Differentiation_Criteria_10'],
                        'Description_10': ext['Description_10']
                    }
                    self.output_data.append(output_row)

        print(f"\n✓ Generated {len(self.output_data)} total 10-digit codes from {i} 8-digit codes")
        return self.save_output()

    def save_output(self) -> str:
        """Save the generated codes to CSV"""
        output_file = '/home/user/naics_12_digits/NAICS_10_DIGIT_CODES.csv'

        fieldnames = [
            'NAICS_6_Digit', 'NAICS_6_Title',
            'NAICS_8_Digit', 'NAICS_8_Title', 'Differentiation_Criteria_8', 'Description_8',
            'NAICS_10_Digit', 'NAICS_10_Title', 'Differentiation_Criteria_10', 'Description_10'
        ]

        with open(output_file, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.output_data)

        print(f"\n✓ Saved to: {output_file}")
        return output_file

def main():
    input_file = '/home/user/naics_12_digits/NAICS_8_DIGIT_CODES.csv'

    if not os.path.exists(input_file):
        print(f"Error: Input file not found: {input_file}")
        return

    generator = NAICS10DigitGenerator(input_file)
    output_file = generator.process_file()

    print("\n" + "="*60)
    print("10-DIGIT NAICS CODE GENERATION COMPLETE")
    print("="*60)

if __name__ == '__main__':
    main()
