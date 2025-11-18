# NAICS 8-Digit Extension Project

## Overview

This project extends the official 6-digit NAICS (North American Industry Classification System) codes to create a more granular 8-digit classification system. The 8-digit extensions provide enhanced precision for business categorization, market research, and industry analysis.

## Project Status

**Current Progress:** 685+ 8-digit codes created across multiple sectors

### Completed Sectors:
- ✅ **Sector 11:** Agriculture, Forestry, Fishing and Hunting (354 8-digit codes)
- ✅ **Sector 21:** Mining, Quarrying, and Oil and Gas Extraction (81 8-digit codes)
- ✅ **Sector 22:** Utilities (42 8-digit codes)
- ✅ **Sector 23:** Construction (117 8-digit codes)
- 🔄 **Sectors 31-33:** Manufacturing (In Progress - 91+ codes added so far)

### Pending Sectors:
- Sector 42: Wholesale Trade
- Sectors 44-45: Retail Trade
- Sectors 48-49: Transportation and Warehousing
- Sector 51: Information
- Sector 52: Finance and Insurance
- Sector 53: Real Estate and Rental and Leasing
- Sector 54: Professional, Scientific, and Technical Services
- Sector 55: Management of Companies and Enterprises
- Sector 56: Administrative and Support Services
- Sector 61: Educational Services
- Sector 62: Health Care and Social Assistance
- Sector 71: Arts, Entertainment, and Recreation
- Sector 72: Accommodation and Food Services
- Sector 81: Other Services (except Public Administration)
- Sector 92: Public Administration

## Methodology

### Extension Principles

Each 8-digit code follows these design principles:

1. **Differentiation Criteria**: Clear basis for subdivision
   - Product Type
   - Service Method
   - Customer Segment (B2B, B2C, B2G)
   - Business Model
   - Production Method
   - Technology/Scale
   - Geographic/Channel

2. **Naming Convention**:
   - Format: `XXXXXX` + `YY` where:
     - `XXXXXX` = Official 6-digit NAICS code
     - `YY` = 2-digit extension (01-99)
   - Example: `111110` (Soybean Farming) → `11111001` (Organic Soybean Farming)

3. **Best Practices**:
   - 5-10 sub-categories per 6-digit code
   - Mutually exclusive categories
   - Clear, descriptive titles
   - Business-relevant distinctions
   - Future-proof structure

## File Structure

```
naics_12_digits/
├── NAICS_8_DIGIT_CODES.csv     # Main data file with all 8-digit extensions
├── README.md                    # This file
└── generate_8_digit_codes.py   # Python utility for code generation
```

## Data Format

The CSV file contains the following columns:

| Column | Description |
|--------|-------------|
| `NAICS_6_Digit` | Official 6-digit NAICS code |
| `NAICS_6_Title` | Official 6-digit NAICS title |
| `NAICS_8_Digit` | Extended 8-digit code |
| `NAICS_8_Title` | Descriptive title for 8-digit code |
| `Differentiation_Criteria` | Basis for subdivision |
| `Description` | Detailed description of the 8-digit category |

## Examples

### Agriculture - Soybean Farming (111110)

| 8-Digit Code | Title | Criteria | Description |
|--------------|-------|----------|-------------|
| 11111001 | Organic Soybean Farming | Production Method | Farms primarily engaged in growing organic soybeans using certified organic farming practices |
| 11111002 | Conventional Soybean Farming | Production Method | Farms primarily engaged in growing soybeans using conventional farming methods |
| 11111003 | Non-GMO Soybean Farming | Product Type | Farms primarily engaged in growing non-genetically modified soybeans |
| 11111004 | GMO Soybean Farming | Product Type | Farms primarily engaged in growing genetically modified soybeans |
| 11111005 | Edamame (Vegetable Soybean) Farming | Product Type | Farms primarily engaged in growing edamame for fresh consumption |
| 11111006 | Identity Preserved Soybean Farming | Business Model | Farms maintaining specific soybean varieties with traceability |
| 11111007 | Soybean Seed Production | Product Type | Farms primarily engaged in growing soybeans for seed production |

### Construction - Residential Remodelers (236118)

| 8-Digit Code | Title | Criteria | Description |
|--------------|-------|----------|-------------|
| 23611801 | Kitchen and Bath Remodeling | Specialty | Residential kitchen and bathroom remodeling |
| 23611802 | Whole House Remodeling | Scope | Complete home renovation and remodeling |
| 23611803 | Basement Finishing | Specialty | Basement remodeling and finishing services |
| 23611804 | Home Addition Construction | Scope | Room additions and home expansions |
| 23611805 | Historic Home Restoration | Specialty | Restoration and renovation of historic homes |

## Research Sources

This classification system was developed leveraging:

1. **Official Sources**:
   - U.S. Census Bureau NAICS definitions and sub-descriptions
   - Economic Census product/service codes
   - Bureau of Labor Statistics industry data

2. **Commercial Taxonomies**:
   - PitchBook industry vertical classifications
   - Data Axle Digital Taxonomy
   - IBISWorld industry reports
   - NAICS HD (High Definition NAICS) - 20,000+ sub-descriptions

3. **Industry Sources**:
   - Trade association classifications
   - Industry-specific taxonomies
   - Market research segmentations

## Use Cases

### Market Research
- Target specific industry niches with precision
- Analyze market trends at granular level
- Identify competitive landscapes

### Business Intelligence
- Enhanced company categorization
- More accurate industry benchmarking
- Improved market sizing

### Risk Assessment
- Differentiate risk profiles within broad industries
- Insurance underwriting and pricing
- Credit risk analysis

### Sales & Marketing
- Precise prospect targeting
- Account-based marketing segmentation
- Lead qualification

## Future Development

### Planned Enhancements:
1. **Complete Coverage**: Extend all 1,057 6-digit codes (~6,500-7,500 total 8-digit codes)
2. **Cross-References**: Mapping to SIC codes, GICS, RBICS, and other classification systems
3. **Search Tool**: Keyword-based code lookup and recommendation engine
4. **API**: RESTful API for programmatic access
5. **Regular Updates**: Quarterly reviews to add emerging industries

## Contributing

This is an ongoing project. Suggestions for:
- Additional granular distinctions
- New emerging industry categories
- Improved naming conventions
- Cross-industry mappings

## License

This classification system is provided for research and commercial use.

## Contact

For questions, suggestions, or collaboration inquiries regarding this NAICS 8-digit extension project.

---

**Last Updated:** November 18, 2025
**Version:** 0.1 (In Development)
**Total Codes:** 685+ (Target: ~6,500-7,500)
