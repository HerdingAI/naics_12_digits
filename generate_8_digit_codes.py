#!/usr/bin/env python3
"""
NAICS 8-Digit Code Generator
Systematically generates 8-digit extensions for all 6-digit NAICS codes
"""

# NAICS 6-digit codes from the user's provided list
NAICS_6_DIGIT_CODES = """
111110	Soybean Farming
111120	Oilseed (except Soybean) Farming
111130	Dry Pea and Bean Farming
111140	Wheat Farming
111150	Corn Farming
111160	Rice Farming
111191	Oilseed and Grain Combination Farming
111199	All Other Grain Farming
111211	Potato Farming
111219	Other Vegetable (except Potato) and Melon Farming
111310	Orange Groves
111320	Citrus (except Orange) Groves
111331	Apple Orchards
111332	Grape Vineyards
111333	Strawberry Farming
111334	Berry (except Strawberry) Farming
111335	Tree Nut Farming
111336	Fruit and Tree Nut Combination Farming
111339	Other Noncitrus Fruit Farming
111411	Mushroom Production
111419	Other Food Crops Grown Under Cover
111421	Nursery and Tree Production
111422	Floriculture Production
111910	Tobacco Farming
111920	Cotton Farming
111930	Sugarcane Farming
111940	Hay Farming
111991	Sugar Beet Farming
111992	Peanut Farming
111998	All Other Miscellaneous Crop Farming
112111	Beef Cattle Ranching and Farming
112112	Cattle Feedlots
112120	Dairy Cattle and Milk Production
112130	Dual-Purpose Cattle Ranching and Farming
112210	Hog and Pig Farming
112310	Chicken Egg Production
112320	Broilers and Other Meat Type Chicken Production
112330	Turkey Production
112340	Poultry Hatcheries
112390	Other Poultry Production
112410	Sheep Farming
112420	Goat Farming
112511	Finfish Farming and Fish Hatcheries
112512	Shellfish Farming
112519	Other Aquaculture
112910	Apiculture
112920	Horses and Other Equine Production
112930	Fur-Bearing Animal and Rabbit Production
112990	All Other Animal Production
113110	Timber Tract Operations
113210	Forest Nurseries and Gathering of Forest Products
113310	Logging
114111	Finfish Fishing
114112	Shellfish Fishing
114119	Other Marine Fishing
114210	Hunting and Trapping
115111	Cotton Ginning
115112	Soil Preparation, Planting, and Cultivating
115113	Crop Harvesting, Primarily by Machine
115114	Postharvest Crop Activities (except Cotton Ginning)
115115	Farm Labor Contractors and Crew Leaders
115116	Farm Management Services
115210	Support Activities for Animal Production
115310	Support Activities for Forestry
211120	Crude Petroleum Extraction
211130	Natural Gas Extraction
212114	Surface Coal Mining
212115	Underground Coal Mining
212210	Iron Ore Mining
212220	Gold Ore and Silver Ore Mining
212230	Copper, Nickel, Lead, and Zinc Mining
212290	Other Metal Ore Mining
212311	Dimension Stone Mining and Quarrying
212312	Crushed and Broken Limestone Mining and Quarrying
212313	Crushed and Broken Granite Mining and Quarrying
212319	Other Crushed and Broken Stone Mining and Quarrying
212321	Construction Sand and Gravel Mining
212322	Industrial Sand Mining
212323	Kaolin, Clay, and Ceramic and Refractory Minerals Mining
212390	Other Nonmetallic Mineral Mining and Quarrying
213111	Drilling Oil and Gas Wells
213112	Support Activities for Oil and Gas Operations
213113	Support Activities for Coal Mining
213114	Support Activities for Metal Mining
213115	Support Activities for Nonmetallic Minerals (except Fuels) Mining
221111	Hydroelectric Power Generation
221112	Fossil Fuel Electric Power Generation
221113	Nuclear Electric Power Generation
221114	Solar Electric Power Generation
221115	Wind Electric Power Generation
221116	Geothermal Electric Power Generation
221117	Biomass Electric Power Generation
221118	Other Electric Power Generation
221121	Electric Bulk Power Transmission and Control
221122	Electric Power Distribution
221210	Natural Gas Distribution
221310	Water Supply and Irrigation Systems
221320	Sewage Treatment Facilities
221330	Steam and Air-Conditioning Supply
236115	New Single-Family Housing Construction (except For-Sale Builders)
236116	New Multifamily Housing Construction (except For-Sale Builders)
236117	New Housing For-Sale Builders
236118	Residential Remodelers
236210	Industrial Building Construction
236220	Commercial and Institutional Building Construction
237110	Water and Sewer Line and Related Structures Construction
237120	Oil and Gas Pipeline and Related Structures Construction
237130	Power and Communication Line and Related Structures Construction
237210	Land Subdivision
237310	Highway, Street, and Bridge Construction
237990	Other Heavy and Civil Engineering Construction
238110	Poured Concrete Foundation and Structure Contractors
238120	Structural Steel and Precast Concrete Contractors
238130	Framing Contractors
238140	Masonry Contractors
238150	Glass and Glazing Contractors
238160	Roofing Contractors
238170	Siding Contractors
238190	Other Foundation, Structure, and Building Exterior Contractors
238210	Electrical Contractors and Other Wiring Installation Contractors
238220	Plumbing, Heating, and Air-Conditioning Contractors
238290	Other Building Equipment Contractors
238310	Drywall and Insulation Contractors
238320	Painting and Wall Covering Contractors
238330	Flooring Contractors
238340	Tile and Terrazzo Contractors
238350	Finish Carpentry Contractors
238390	Other Building Finishing Contractors
238910	Site Preparation Contractors
238990	All Other Specialty Trade Contractors
"""

# Construction extensions
CONSTRUCTION_EXTENSIONS = {
    "236115": [
        ("23611501", "Spec Home Construction", "Business Model", "Construction of single-family homes on speculation"),
        ("23611502", "Custom Home Construction Contracting", "Business Model", "General contracting for custom single-family homes"),
        ("23611503", "Green/LEED Home Construction", "Specialty", "Energy-efficient and certified green home construction"),
    ],
    "236116": [
        ("23611601", "Apartment Building Construction", "Building Type", "Construction of multi-unit apartment buildings"),
        ("23611602", "Condominium Construction", "Building Type", "Construction of condominium complexes"),
        ("23611603", "Affordable Housing Construction", "Market Segment", "Construction of affordable/subsidized multi-family housing"),
    ],
    "236117": [
        ("23611701", "Production Home Builders", "Business Model", "Large-scale production homebuilding operations"),
        ("23611702", "Townhome For-Sale Builders", "Building Type", "Builders constructing townhomes for direct sale"),
        ("23611703", "Luxury Home Builders", "Market Segment", "High-end custom home builders for sale"),
    ],
    "236118": [
        ("23611801", "Kitchen and Bath Remodeling", "Specialty", "Residential kitchen and bathroom remodeling"),
        ("23611802", "Whole House Remodeling", "Scope", "Complete home renovation and remodeling"),
        ("23611803", "Basement Finishing", "Specialty", "Basement remodeling and finishing services"),
        ("23611804", "Home Addition Construction", "Scope", "Room additions and home expansions"),
    ],
    "236210": [
        ("23621001", "Manufacturing Plant Construction", "Facility Type", "Construction of manufacturing facilities"),
        ("23621002", "Warehouse and Distribution Center Construction", "Facility Type", "Construction of industrial warehouses and distribution centers"),
        ("23621003", "Food Processing Plant Construction", "Facility Type", "Construction of food and beverage processing facilities"),
        ("23621004", "Data Center Construction", "Facility Type", "Construction of data centers and server facilities"),
    ],
    "236220": [
        ("23622001", "Office Building Construction", "Building Type", "Construction of commercial office buildings"),
        ("23622002", "Retail Center Construction", "Building Type", "Construction of shopping centers and retail facilities"),
        ("23622003", "Hotel and Hospitality Construction", "Building Type", "Construction of hotels and lodging facilities"),
        ("23622004", "Healthcare Facility Construction", "Building Type", "Construction of hospitals clinics and medical buildings"),
        ("23622005", "Educational Facility Construction", "Building Type", "Construction of schools and educational buildings"),
        ("23622006", "Religious Building Construction", "Building Type", "Construction of churches and religious facilities"),
    ],
}

# This will be expanded with all remaining sectors
print("NAICS 8-Digit Code Generator initialized")
print(f"Total 6-digit codes to process: {len(NAICS_6_DIGIT_CODES.strip().split(chr(10)))}")
