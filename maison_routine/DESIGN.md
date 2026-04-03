# Design System: Tactile Minimalism & Quiet Luxury

## 1. Overview & Creative North Star
The Creative North Star for this design system is **"The Curated Atelier."** 

This system rejects the frantic, cluttered nature of traditional e-commerce. Instead, it treats the digital interface as a high-end physical space—think of a sun-drenched, limestone-floored resort boutique where every garment is given room to breathe. We move beyond the "template" look by utilizing intentional asymmetry, oversized whitespace, and a "tonal-first" philosophy that prioritizes texture and light over rigid borders and lines.

## 2. Colors & Atmospheric Depth
The palette is rooted in a sophisticated, low-contrast harmony that mimics natural linen and soft studio lighting.

### Tonal Strategy
- **Background (`#F9F9F9`)**: Not a stark white, but a warm, "creamy" off-white that feels like heavy-weight paper.
- **Accent (`#D2A7A7`)**: A dusty mauve used sparingly for moments of soft guidance or quiet celebration.
- **Action/Text (`#222222`)**: A matte black that provides an authoritative, editorial anchor to the airy surroundings.

### The "No-Line" Rule
**Explicit Instruction:** 1px solid borders are strictly prohibited for sectioning. We define space through background shifts. A `surface-container-low` section sitting on a `surface` background is the only way to denote a change in context. Borders are a crutch; light and shadow are the tools of a director.

### Surface Hierarchy & Glassmorphism
Utilize the `surface-container` tiers to create "nested" depth. 
- **The Glass Principle:** For floating elements (navigation bars, quick-view modals), apply a semi-transparent background using the `surface-variant` token with a `backdrop-blur` of 20px. 
- **Signature Gradients:** To give CTAs "visual soul," use a subtle linear gradient from `primary` (#605F5F) to `primary-container` (#E5E2E1) at a 45-degree angle. This mimics the way light hits a textured knit.

## 3. Typography: Editorial Authority
The typography system uses **Inter** (or Montserrat as a fallback) to create an experience that feels more like a fashion magazine than a web app.

- **Display & Headlines:** Use `display-lg` to `headline-sm` with a tight tracking (-0.02em) to feel impactful yet refined. 
- **Body:** `body-lg` (1rem) is the standard. It must maintain a wide line height (1.6 to 1.8) to maximize legibility and "airiness."
- **The Signature Action Label:** All interactive buttons must use **ALL CAPS** with a `1.2px` letter spacing. This transforms a simple command into a curated call to action.

## 4. Elevation & Depth: The Layering Principle
We do not use elevation to make things "pop"; we use it to create a soft, natural lift.

- **Ambient Shadows:** For product cards, use a radius of `14px` (`xl` scale). Shadows must be "extra-diffused": `box-shadow: 0 20px 40px rgba(34, 34, 34, 0.05)`. The shadow is not grey; it is a 5% opacity version of our Matte Black, mimicking a softbox light in a studio.
- **Tonal Layering:** Place a `surface-container-lowest` card (Pure White) on a `surface-container-low` section. This creates a "Paper-on-Stone" effect that is much more premium than a stroke.
- **Ghost Borders:** If a boundary is legally or functionally required, use the `outline-variant` token at **15% opacity**. Anything higher is considered visual noise.

## 5. Components

### Buttons
- **Primary:** Matte Black (`#222222`) background, white text, `6px` radius. Size: 48px height for tactile ease.
- **Secondary:** Surface background with a "Ghost Border."
- **Tertiary:** Text-only, All-Caps, 1.2px letter spacing with a subtle underline that appears only on hover.

### Product Cards
- **Construction:** 14px radius, no border. 
- **Image Treatment:** Use a "High-End Studio" crop. Avoid centered, flat product shots. Use slightly off-center compositions to evoke movement.
- **Spacing:** Use `spacing-4` (1.4rem) between the image and the product metadata.

### Input Fields
- **Style:** Underline-only or very soft-filled (`surface-container-high`).
- **Interaction:** On focus, the label should shift to `secondary` (Mauve) and the underline should transition from 10% opacity to 100% matte black.

### Navigation & Lists
- **Divider Prohibition:** Never use horizontal rules. Use `spacing-8` (2.75rem) to separate list items or subtle background shifts.
- **Tactile Feedback:** Every interaction should have a 300ms ease-in-out transition. Luxury is never abrupt.

## 6. Do's and Don'ts

### Do:
- **Embrace Asymmetry:** Let images bleed off the edge or stagger text blocks to create a "custom-built" feel.
- **Use Wide Margins:** Use `spacing-20` (7rem) for page gutters. Compression is the enemy of luxury.
- **Focus on Texture:** Use high-resolution imagery of linen, knitwear, and silk. The UI should feel like it has a "scent."

### Don't:
- **Don't use pure black shadows:** It muddies the off-white background.
- **Don't use standard icons:** If an icon is needed, use ultra-thin (1pt) stroke weights.
- **Don't use 100% opaque borders:** They break the "Quiet Luxury" illusion and feel like a budget framework.
- **Don't crowd the footer:** The footer should be as airy as the hero section, utilizing `title-sm` for headers.

---
*Note: This design system is a living document. Every update should be filtered through the lens of "The Curated Atelier." If it feels fast, loud, or crowded, it does not belong.*