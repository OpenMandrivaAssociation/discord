%global         debug_package %{nil}
%global         __strip /bin/true
%global         __requires_exclude libffmpeg.so
%global         _build_id_links none
%global __provides_exclude_from %{_libdir}/discord/.*\\.s

Name:           discord
Version:        0.0.42
Release:        1
Summary:        All-in-one voice and text chat for gamers

# License Information: https://bugzilla.rpmfusion.org/show_bug.cgi?id=4441#c14
License:        Proprietary
URL:            https://discordapp.com/
Source0:        https://dl.discordapp.net/apps/linux/%{version}/%{name}-%{version}.tar.gz
ExclusiveArch:  %{x86_64}

BuildRequires:  desktop-file-utils

Recommends:     google-noto-emoji-color-fonts

%description
Linux Release for Discord, a free proprietary VoIP application designed for
gaming communities.

Given the non-free nature, it is recommended to use an open alternative,
such as Mumble.

%prep
%autosetup -p1 -n Discord

%build

%install
mkdir -p %{buildroot}/%{_bindir}/
mkdir -p %{buildroot}/%{_libdir}/discord
mkdir -p %{buildroot}/%{_datadir}/applications

desktop-file-install                            \
--set-icon=%{name}                              \
--set-key=Exec --set-value=%{_bindir}/Discord   \
--delete-original                               \
--dir=%{buildroot}/%{_datadir}/applications     \
discord.desktop

cp -r * %{buildroot}/%{_libdir}/discord/
ln -sf ../%{_lib}/discord/Discord %{buildroot}/%{_bindir}/
install -p -D -m 644 %{name}.png \
        %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{name}.png

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%files
%{_libdir}/discord/
%{_bindir}/Discord
%{_datadir}/applications/discord.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
