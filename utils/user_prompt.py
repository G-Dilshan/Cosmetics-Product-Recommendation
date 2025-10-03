from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate

# Define the human message template - FIXED VERSION
human_message = HumanMessagePromptTemplate.from_template("""
User's skin concerns: {concerns}

Here is the available skincare product catalog from Bobbi Brown Cosmetics:

[
  {{
    "name": "Vitamin Enriched Face Base Moisturizer & Primer",
    "category": "Moisturizer",
    "price": "$113.00",
    "image_url": "https://www.bobbibrowncosmetics.com/media/export/cms/products/responsive/bb_sku_E1LM01_1x1_0.png",
    "description": "{{
        "what it is": "Skincare made for makeup. Our bestselling hydrating primer instantly nourishes, plumps, and preps skin to improve the look of foundation. It's full makeup prep in one step, blending the performance of a makeup primer with the cushion of a moisturizer.",
        "who it's for": "Normal to oily skin types.",
        "key ingredients": "Shea Butter"
    }}",
    "skin_types": ["Normal to oily skin types"],
    "size": "100ml",
    "product_url": "https://www.bobbibrowncosmetics.com/product/14007/7485/skincare/moisturizer/vitamin-enriched-face-base-moisturizer-primer"
  }},
  {{
    "name": "Extra Repair Moisture Cream Intense",
    "category": "Moisturizer",
    "price": "$118.00",
    "image_url": "https://www.bobbibrowncosmetics.com/media/export/cms/products/responsive/bb_sku_EREP01_1x1_0.png",
    "description": "{{
        "what it is": "An ultra-hydrating face cream that replenishes and smooths skin. Formulated with our Extra Repair Complex and Vitamin C, this luxurious cream instantly plumps the skin with moisture to reduce the appearance of fine lines.",
        "how it works": "Extra Repair Complex, with Argireline Peptide, and Vitamin C, helps support skin's natural collagen production to reduce the look of fine lines over time.
        Acetyl Glucosamine helps smooth skin and diminish the appearance of pores over time. Hyaluronic Acid, Glycerin, and Shea Butter work to hydrate, plump, and condition skin.
        Vitamin E Complex provides antioxidant benefits and helps protect skin from the effects of blue light.Refillable packaging is designed to be reused and recycled.",
    }}",
    "size": "50ml",
    "product_url": "https://www.bobbibrowncosmetics.com/product/14007/93885/skincare/moisturizer/extra-repair-moisture-cream-intense/fh21"
  }},
  {{
    "name": "Soothing Cleansing Oil Facial Cleanser",
    "category": "Cleansers & Toners",
    "price": "$39.00",
    "image_url": "https://www.bobbibrowncosmetics.com/media/export/cms/products/responsive/bb_sku_EWR001_1x1_0.png",
    "description": "{{
        "what is it": "A water-light oil facial cleanser and makeup remover that removes impurities and waterproof makeup while nourishing skin.
        Free of: Drying alcohol, Animal derived ingredients ,Vegetarian Formaldehyde and its donors, Gluten ,Mineral oil, Parabens, Paraffins, Petrolatum, Phthalates ,Silicone, Sulfates SLS/SLES -or- Sulfate cleansers ,Sulfite ,Synthetic color ,Synthetic fragrance ,Triclocarban",
        "how to use": "Massage onto dry skin with dry hands, starting at cheeks, then nose, forehead, temples, jawline, chin, and upper lip. Gently sweep across closed eyes and lips. Wet hands, then massage again to emulsify. Rinse and pat dry.",
    }}",
    "size": "100ml",
    "product_url": "https://www.bobbibrowncosmetics.com/product/14013/123703/skincare/cleansers-toners/soothing-cleansing-oil-facial-cleanser"
  }},
  {{
    "name": "Extra Cleansing Balm",
    "category": "Cleansers & Toners",
    "price": "$68.00",
    "image_url": "https://www.bobbibrowncosmetics.com/media/export/cms/products/responsive/bb_sku_ERAN01_1x1_0.png",
    "description": "{{
        "what is it": "A conditioning makeup cleansing balm that melts away impurities and long-wear eye and lip makeup while leaving skin nourished and cushioned. This balm cleanser is a treat for the senses with an Orange Oil-infused formula scented with uplifting notes of citrus.",
        "how it works": "Extra-rich balm dissolves face makeup and impurities,Olive Extract and Glycerin help nourish and cushion,Orange Oil wakes up the senses with uplifting notes of citrus",
        "how to use": "Warm up in dry hands then gently massage over dry skin in circular motions to melt away makeup and impurities. Avoid eye area. Rinse away, then pat dry. Follow with the rest of your skincare regimen.",
        "key ingredients": "Olive Extract, Glycerin, Orange Oil"
    }}"
    "size": "100ml",
    "product_url": "https://www.bobbibrowncosmetics.com/product/14013/93887/skincare/cleansers-toners/extra-cleansing-balm/fh21"
  }},
  {{
    "name": "Vitamin Enriched Smoothing Serum",
    "price": "$86.00",
    "image_url": "https://www.bobbibrowncosmetics.com/media/export/cms/products/responsive/bb_sku_ETY101_1x1_0.png",
    "description": "{{
        "what is it": "Niacinamide and Vitamin C 2-in-1 smoothing serum and glow essence boosts moisture and radiance while brightening dark spots and prepping skin for seamless makeup application.
        What else you need to know: Infused with 10 potent skin-caring ingredients, this multitasking formula gives skin an overnight moisture boost and a fresh, hydrated glow while helping smooth and even skin texture. When used with Vitamin Enriched Face Base, it helps plump skin and smooth makeup application.
        Highlighted Ingredients: Niacinamide (Vitamin B3) helps provide long-term hydration.
        Vitamin C: helps fight dullness and delivers skin-tone-brightening benefits over time 
        HydroGlow Fruit Complex and Cactus Flower help provide long-term moisturization for a hydrated, healthy-looking glow.",
        "how it works": "This fast-absorbing milky serum-essence smooths the look and feel of skin  through resurfacing and  delivers long-term moisturization for a fresh, hydrated glow. When used with Vitamin Enriched Face Base and Vitamin Enriched Eye Base, it helps plump skin and smooth makeup application.  Plus, the bright signature citrus scent of Grapefruit and Geranium Oils uplifts and refreshes the senses.",
    }}"
    "size": "30ml",
    "product_url": "https://www.bobbibrowncosmetics.com/product/14015/124182/skincare/serums-treatments/vitamin-enriched-smoothing-serum"
  }},
  {{
    "name": "Extra Face Oil",
    "category": "Serums & Treatments",
    "price": "$80.00",
    "image_url": "https://www.bobbibrowncosmetics.com/media/export/cms/products/responsive/bb_sku_E1YJ01_1x1_0.png",
    "description": "{{
        "what it is": "A lightweight facial oil that nourishes and comforts dry skin. Softens and conditions with a quick-absorbing blend of Sesame, Sweet Almond, Olive, and Jojoba Oils.",
        "who it's for": "Anyone with normal to extra dry skin.",
        "how it works": "Sesame, Sweet Almond, Olive, and Jojoba Oils help keep skin soft and supple over time. Aromatic blend of Natural Essential Oils, including Neroli, Patchouli, Lavender, and Sandalwood, uplifts the senses. Dermatologist-tested.",
    }}"
    "size": "30ml",
    "product_url": "https://www.bobbibrowncosmetics.com/product/14015/8100/skincare/serums-treatments/extra-face-oil"
  }},
  {{
    "name": "Primer Plus Protection SPF 50",
    "category": "primer",
    "price": "$52.00",
    "image_url": "https://www.bobbibrowncosmetics.com/media/export/cms/products/responsive/bb_sku_EKLT01_1x1_0.png",
    "description": "{{
        "what it is": "A lightweight, fast-absorbing face primer with SPF. Provides invisible broad-spectrum UVA/UVB protection.",
        "how it works": "Face primer with broad-spectrum UVA and UVB protection helps prevent sun damage and premature signs of aging. Fast-absorbing formula applies evenly and invisibly.",
        "how to use": "After your skincare routine, smooth primer all over face, avoiding eye area, and then apply foundation."
    }}",
    "size": "40ml",
    "product_url": "https://www.bobbibrowncosmetics.com/product/22040/58333/makeup/face/primer/primer-plus-protection-spf-50/fh18"
  }},
  {{
    "name": "Hydrating Face Toner",
    "category": "Cleansers & Toners",
    "price": "$44.00",
    "image_url": "https://www.bobbibrowncosmetics.com/media/export/cms/products/responsive/bb_sku_E65R01_1x1_0.png",
    "description": "{{
        "what it is": "A hydrating face toner that restores and balances skin's moisture. Apply toner after cleansing to leave your skin soft, smooth, and well-prepped for further treatments.",
        "who it's for": "Anyone who wants to add a refreshingly hydrating step to their skincare routine can use the face toner, especially those with dry or sensitive skin.",
        "how it works": "Our signature formula, infused with Enriched Mineral Water Blend, Cucumber, Chamomile, Licorice, Aloe Leaf, and Lavender, leaves skin feeling smooth, soft, and conditioned. Face toner balances and prepares skin for the next treatment step.",
        "how to use": "Apply hydrating toner to face, morning and night. For combination-oily skin, use a cotton pad to sweep onto face. For drier skin, use your hands to massage into skin."
    }}",
    "size": "200ml",
    "product_url": "https://www.bobbibrowncosmetics.com/product/14013/12768/skincare/cleansers-toners/hydrating-face-toner/fh10"
  }},
  {{
    "name": "Hydrating Eye Cream",
    "category": "Eye Care",
    "price": "$66.00",
    "image_url": "https://www.bobbibrowncosmetics.com/media/export/cms/products/responsive/bb_sku_E65Y01_1x1_0.png",
    "description": "{{
        "what it is": "A refreshing and hydrating under eye cream that leaves the under eye area plumped and perfectly prepped for makeup.",
        "who it's for": "Anyone looking for a lightweight, soothing eye cream to wear on its own or layered under concealer for a flawless finish.",
        "how it works": "Jojoba Seed Oil, Avocado Oil, and Squalane help skin feel comforted and conditioned. Quick-absorbing formula helps create a smooth, hydrated base for concealer.",
        "how to use": "Apply with ring finger, patting gently under eye."
    }}",
    "size": "15ml",
    "product_url": "https://www.bobbibrowncosmetics.com/product/14008/12762/skincare/eye-care/hydrating-eye-cream/fh10"
  }},
  {{
    "name": "Extra Illuminating Moisture Balm",
    "category": "Moisturizer",
    "price": "$87.00",
    "image_url": "https://www.bobbibrowncosmetics.com/media/export/cms/products/responsive/bb_sku_EHP201_1x1_0.png",
    "description": "{{
        "what it is": "A highlighter moisturizer that instantly illuminates with pearl particles for glowing skin. This lightweight moisturizer softens and plumps with skincare ingredients including Hyaluronic Acid, Shea Butter, and Murumuru Seed Butter.",
        "how it works": "Microfine Pearls instantly boost radiance. Hyaluronic Acid helps instantly hydrate and plump. Shea Butter helps condition skin, while Murumuru Seed Butter helps strengthen skin's protective barrier.",
        "how to use": "Apply as an illuminating moisturizer on bare skin or over skincare for a lit-from-within glow. Layer over foundation for a radiant finish."
    }}",
    "size": "30ml",
    "product_url": "https://www.bobbibrowncosmetics.com/product/14007/55025/skincare/moisturizer/extra-illuminating-moisture-balm"
  }}
]

Based on the user's skin concerns provided above, recommend the most suitable products from this catalog. Return the recommendations strictly in JSON format with fields: product_name, description, image_url, price, and why_it_matches.

Format your response as:
```json
[
  {{
    "product_name": "Product Name",
    "description": "Product description",
    "image_url": "Product image URL", 
    "product_url": "Product URL",
    "price": "Product price",
    "why_it_matches": "Explanation of why this product matches the user's skin concerns"
  }}
]
```
""")

# vision_prompt = """
# Analyze the provided facial image and identify visible skin concerns, aesthetic conditions, lip concerns, around eye concerns and overall skin characteristics.
# Categorized the face into forehead, temples, periorbital area, cheeks, nose, perioral area, chin, jawline, ears, scalp and lips.
# Provide a comprehensive assessment for each category in JSON format.
# """

vision_prompt = """
Analyze the provided facial image and provide a comprehensive assessment of visible skin, aesthetic, and specific area concerns.
The assessment must be provided in a single JSON object with the following structure and content requirements:

Categorization: The face must be divided into the following key anatomical and aesthetic areas: full_face, forehead, temples, periorbital_area, cheeks, nose, perioral_area, chin, jawline, ears, scalp, and lips.

Content for Each Category:
For the full_face category, include a detailed overall_assessment describing the general skin type, texture, tone, and major aesthetic conditions observed across the entire face.
For all other anatomical categories, provide a detailed assessment listing all visible concerns (e.g., fine lines, wrinkles, acne, redness, volume loss, pigmentation, sun damage, pore size, texture issues).

Ratings:
For the full_face category, include a rating property, which is a numerical score out of 100 representing the overall skin health and aesthetic appearance.
For all other anatomical categories, include a rating property, which is a numerical score out of 100 representing the health and aesthetic condition of that specific area.

JSON Format Example Structure:
{
  "full_face": {
    "rating": 75,
    "overall_assessment": "Combination skin type with visible sun damage, mild acne, and moderate loss of volume, contributing to a tired appearance."
  },
  "forehead": {
    "rating": 80,
    "assessment":
  },
  "periorbital_area": {
    "rating": 65,
    "assessment": 
  },
  "lips": {
    "rating": 70,
    "assessment": 
  },
  // ... (Include all 12 categories: full_face, forehead, temples, periorbital_area, cheeks, nose, perioral_area, chin, jawline, ears, scalp, lips)
}
"""