#!/usr/bin/env python3

"""
Demo of Playwright browser automation with Python
Converted from Playwright TypeScript to Python
Please see the file README.md for more information.

## Tracking

  * Package: demo-playwright-python
  * Version: 1.4.0
  * Created: 2019-11-02T00:00:00Z
  * Updated: 2025-04-24T13:58:02Z
  * License: GPL-2.0-or-greater or for custom license contact us
  * Contact: Joel Parker Henderson (joel@joelparkerhenderson.com)
"""

# Import Playwright types and functions
from playwright.sync_api import sync_playwright, Browser, BrowserContext, Page, Locator
from typing import Optional
import sys

def demo() -> None:
    """Main demo function showing Playwright automation examples."""
    
    with sync_playwright() as p:
        # Initialize browser with options similar to Selenium setup
        browser: Browser = p.chromium.launch(
            headless=False,  # Set to True for headless mode
            args=[
                '--verbose',  # Enable verbose logging
                '--disable-notifications',  # Disable notifications such as popups
            ]
        )
        
        # Create a new context with preferences
        context: BrowserContext = browser.new_context(
            # Reject cookies (Playwright doesn't have direct cookie rejection, 
            # but you can clear cookies or use context isolation)
            accept_downloads=False,
            # Additional context options can be set here
        )
        
        # Create a new page
        page: Page = context.new_page()
        
        try:
            # Navigate to a website
            page.goto("https://testingexamples.github.io")
            
            ###
            # Find elements in various ways.
            # Note: Playwright uses locators which auto-wait and retry
            ###
            
            # Find an element by id.
            #
            # This demonstrates locator with id selector.
            #
            # Example HTML:
            #
            #      <p id="id-example-1">Lorem Ipsum</p>
            #
            element_by_id: Locator = page.locator('#id-example-1')
            outer_html_by_id: str = element_by_id.evaluate('(el) => el.outerHTML')
            print(outer_html_by_id)
            
            # Find an element by name attribute.
            #
            # This demonstrates locator with attribute selector.
            #
            # Example HTML:
            #
            #     <p name="name-example-1">Lorem Ipsum</p>
            #
            element_by_name: Locator = page.locator('[name="name-example-1"]')
            outer_html_by_name: str = element_by_name.evaluate('(el) => el.outerHTML')
            print(outer_html_by_name)
            
            # Find an element by class name.
            #
            # This demonstrates locator with class selector.
            #
            # Example HTML:
            #
            #     <p class="class-example-1">Lorem Ipsum</p>
            #
            element_by_class_name: Locator = page.locator('.class-example-1')
            outer_html_by_class: str = element_by_class_name.evaluate('(el) => el.outerHTML')
            print(outer_html_by_class)
            
            # Find an element that is a link by its text.
            #
            # This demonstrates locator with text selector.
            #
            # Example HTML:
            #
            #     <a href="https://example.com">Link Example 1</a>
            #
            element_by_link_text: Locator = page.locator('a', has_text='Link Example 1')
            # Alternative: page.locator('text="Link Example 1"') for exact text
            outer_html_by_link: str = element_by_link_text.evaluate('(el) => el.outerHTML')
            print(outer_html_by_link)
            
            # Find an element by XPath query.
            #
            # This demonstrates XPath selector.
            #
            # Example HTML:
            #
            #     <input type=submit>
            #
            element_by_xpath: Locator = page.locator('xpath=//input[@type="submit"]')
            outer_html_by_xpath: str = element_by_xpath.evaluate('(el) => el.outerHTML')
            print(outer_html_by_xpath)
            
            ###
            # Interact with form inputs in various ways.
            ###
            
            # Type in a text input.
            #
            # Example HTML:
            #
            #     <input type="text" id="text-example-1">
            #
            text: Locator = page.locator('#text-example-1-id')
            text_outer_html: str = text.evaluate('(el) => el.outerHTML')
            print(text_outer_html)
            text.fill("hello")
            # Alternative: text.type("hello") for character-by-character typing
            
            # Click a checkbox input.
            #
            # Example HTML:
            #
            #     <input type="checkbox" id="checkbox-example-1-id">
            #
            checkbox: Locator = page.locator('#checkbox-example-1-id')
            checkbox_outer_html: str = checkbox.evaluate('(el) => el.outerHTML')
            print(checkbox_outer_html)
            checkbox.check()
            # Alternative: checkbox.click() also works
            
            # Click a radio input.
            #
            # Example HTML:
            #
            #     <input type="radio" id="radio-example-1-id-option-1-id">
            #
            radio: Locator = page.locator('#radio-example-1-option-1-id')
            radio_outer_html: str = radio.evaluate('(el) => el.outerHTML')
            print(radio_outer_html)
            radio.check()
            # Alternative: radio.click() also works
            
            # Choose a select input option.
            #
            # Example HTML:
            #
            #     <select id="select-example-1-id">
            #       <option>alfa</option>
            #       <option>bravo</option>
            #       <option>charlie</option>
            #     </select>
            #
            select_element: Locator = page.locator('#select-example-1-id')
            select_outer_html: str = select_element.evaluate('(el) => el.outerHTML')
            print(select_outer_html)
            
            # Select by index (0-based)
            select_element.select_option(index=0)
            
            # Get the selected option value
            selected_value: str = select_element.input_value()
            print(f"Selected option value: {selected_value}")
            
            # To get the selected option element HTML (similar to Selenium's getFirstSelectedOption)
            selected_option: Locator = select_element.locator('option:checked')
            selected_option_html: str = selected_option.evaluate('(el) => el.outerHTML')
            print(selected_option_html)
            
            # Alternative selection methods with proper typing:
            # select_element.select_option('alfa')  # by value or text
            # select_element.select_option(label='alfa')  # by visible text
            # select_element.select_option(value='alfa')  # by value attribute
            
        except Exception as err:
            print(f"Error message: {err}")
            import traceback
            print(f"Stack trace:\n{traceback.format_exc()}")
            
        finally:
            # Close browser
            browser.close()


def demo_async() -> None:
    """
    Alternative async implementation using playwright.async_api
    Uncomment to use the async version instead.
    """
    # import asyncio
    # from playwright.async_api import async_playwright
    # 
    # async def run():
    #     async with async_playwright() as p:
    #         browser = await p.chromium.launch(headless=False)
    #         context = await browser.new_context(accept_downloads=False)
    #         page = await context.new_page()
    #         
    #         try:
    #             await page.goto("https://testingexamples.github.io")
    #             # ... rest of the code with await prefixes
    #         finally:
    #             await browser.close()
    # 
    # asyncio.run(run())
    pass


def main() -> None:
    """Main entry point with error handling."""
    try:
        demo()
    except Exception as err:
        print(f"Fatal error: {err}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    # Execute main function when script is run directly
    main()