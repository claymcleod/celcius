import sys,os
import curses

__version__ = '0.1'
LINE_FEED = 10

def draw_status_bar(stdscr):

        statusbarstr = "Press 'q' to exit"
        height, width = stdscr.getmaxyx()

        # Render status bar
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(height-1, 0, statusbarstr)
        stdscr.addstr(height-1, len(statusbarstr), " " * (width - len(statusbarstr) - 1))
        stdscr.attroff(curses.color_pair(3))

def draw_menu(stdscr):
    k = 0

    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    # Start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # Loop where k is the last character pressed
    while (k != ord('c')):

        # Initialization
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        # Declaration of strings
        title = "Celcius Version {}".format(__version__)[:width-1]
        subtitle = "Written by Clay McLeod (github.com/claymcleod)"[:width-1]
        licensestr = "Released under the MIT License"[:width-1]
        continuestr = "Press 'c' to continue..."[:width-1]

        # Centering calculations
        start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
        start_x_subtitle = int((width // 2) - (len(subtitle) // 2) - len(subtitle) % 2)
        start_x_licensestr = int((width // 2) - (len(licensestr) // 2) - len(licensestr) % 2)
        start_x_continuestr = int((width // 2) - (len(continuestr) // 2) - len(continuestr) % 2)
        start_y = int((height // 2) - 2)

        # Draw statusbar
        draw_status_bar(stdscr)

        # Turning on attributes for title
        stdscr.attron(curses.color_pair(2))
        stdscr.attron(curses.A_BOLD)

        # Rendering title
        stdscr.addstr(start_y, start_x_title, title)

        # Turning off attributes for title
        stdscr.attroff(curses.color_pair(2))
        stdscr.attroff(curses.A_BOLD)

        # Print rest of text
        stdscr.addstr(start_y + 1, start_x_subtitle, subtitle)
        stdscr.addstr(start_y + 2, start_x_licensestr, licensestr)
        stdscr.addstr(start_y + 4, (width // 2) - 2, '-' * 4)
        stdscr.addstr(start_y + 6, start_x_continuestr, continuestr)

        # Refresh the screen
        stdscr.refresh()

        # Wait for next input
        k = stdscr.getch()

        if k == ord('q'):
            sys.exit(1)

    menu_offset_x = 5
    menu_offset_y = 2
    current_selection = 0
    options = ["Hello", "There", "World"]

    while k != ord('q'):
        stdscr.clear()
        draw_status_bar(stdscr)

        for i in range(len(options)):
            the_menu_str = '{}. {}'.format(i, options[i])
            stdscr.addstr(menu_offset_y+i, menu_offset_x, the_menu_str)

        if k == curses.KEY_DOWN or k == curses.KEY_RIGHT:
            current_selection = min(current_selection + 1, len(options) - 1)
        elif k == curses.KEY_UP or k == curses.KEY_LEFT:
            current_selection = max(current_selection - 1, 0)
        elif k == LINE_FEED:
            os.system('touch ~/{}.txt'.format(options[current_selection]))
            sys.exit(1)

        stdscr.move(menu_offset_y+current_selection, menu_offset_x)

        stdscr.refresh()
        k = stdscr.getch()

def main():
    curses.wrapper(draw_menu)

if __name__ == "__main__":
    main()
